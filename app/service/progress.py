from db.models.status import Status
from db.constants import IN_PROGRESS, CLOSED
from db.models import UserPath, User, UserModuleProgress
from service import roadmap, exception
from hashlib import sha256
from schemas import skill_schema
from tortoise.exceptions import IntegrityError
from tortoise.transactions import in_transaction
from tortoise import Tortoise


async def get_learned_skills(user_id: int) -> list[str]:
    learned_skills = await UserModuleProgress.filter(
        user_id=user_id, status_id=CLOSED
    ).all()
    return [s.module_code for s in learned_skills]


async def create_user_path(
    user_id: int, target_skills: list[str]
) -> skill_schema.UserPath:
    learned_skills = await UserModuleProgress.filter(
        user_id=user_id, status_id=CLOSED
    ).all()
    path = await roadmap.get_roadmap(
        [s.module_code for s in learned_skills], target_skills
    )
    hash_object = sha256(path.model_dump_json().encode())
    path_hash = hash_object.hexdigest()

    async with in_transaction() as conn:
        user = await User.select_for_update(using_db=conn).get_or_none(id=user_id)
        if user is None:
            raise exception.NotFoundError("user")
        if user.have_active_path:
            raise exception.AlreadyExist("active roadmap")

        current_module_code = None
        module_path_id = 0
        if path and path.path:
            current_module_code = path.path[module_path_id].id
        else:
            raise exception.NotFoundError("generate path")

        lenght = len(path.path)
        try:
            await UserPath.create(
                using_db=conn,
                user_id=user_id,
                path=path.model_dump(),
                path_hash=path_hash,
                current_module_code=current_module_code,
                current_step=module_path_id,
                path_len=lenght,
            )
        except IntegrityError:
            raise exception.AlreadyExist("path")

        user.have_active_path = True
        await user.save(update_fields=["have_active_path"], using_db=conn)

        return skill_schema.UserPath(
            complited=module_path_id,
            current_module=current_module_code,
            lenght=lenght,
            path=path.path,
        )


async def get_current_user_path(user_id: int) -> skill_schema.UserPath:
    user_path = await UserPath.get_or_none(user_id=user_id, status=IN_PROGRESS)
    if user_path is None:
        raise exception.NotFoundError("active user path")
    return skill_schema.UserPath(
        complited=user_path.current_step,
        current_module=user_path.current_module_code,
        lenght=user_path.path_len,
        path=[
            skill_schema.ModuleOut.model_validate(m) for m in user_path.path.get("path")
        ],
    )


async def get_next_step(module_code: str, user_id: int):
    conn = Tortoise.get_connection("default")
    next_step = await conn.execute_query(
        """
        WITH subquery AS (SELECT 
            elem.value as value, LEAD(elem.value, 1) OVER (ORDER BY elem.ord) as next_value, userpath.user_id
        FROM userpath,
        LATERAL jsonb_array_elements(userpath.path->'path') WITH ORDINALITY AS elem(value, ord)
        )
        SELECT subquery.next_value
        FROM subquery
        WHERE subquery.value->>'id' = $1 AND subquery.next_value IS NOT NULL AND subquery.user_id = $2;

        """,
        [module_code, user_id],
    )
    if next_step[0] == 0:
        raise exception.NotFoundError("active roadmap")
    return skill_schema.ModuleOut.model_validate_json(next_step[1][0].get("next_value"))


async def update_progress(user_id: int, module_code: str):
    async with in_transaction() as conn:
        user_path = (
            await UserPath.select_for_update(using_db=conn)
            .filter(
                user_id=user_id,
                status=IN_PROGRESS,
            )
            .first()
        )
        if user_path is None:
            raise exception.NotFoundError("module in active path")

        if user_path.current_module_code != module_code:
            raise exception.BadRequest(
                detail=f"Cant complite '{module_code}', current module is '{user_path.current_module_code}'. "
            )

        await UserModuleProgress.update_or_create(
            user_id=user_id,
            module_code=module_code,
            defaults={
                "status_id": CLOSED,
                "user_id": user_id,
                "module_code": module_code,
            },
        )

        nex_step = user_path.current_step + 1
        if nex_step >= user_path.path_len:
            s = await Status.get(using_db=conn, id=CLOSED)
            user_path.status = s
            user_path.current_step = nex_step
            await User.filter(id=user_id).update(have_active_path=False)

        else:
            path_list: list[dict[str, str]] = user_path.path.get("path", [])
            user_path.current_module_code = path_list[nex_step].get("id")
            user_path.current_step = nex_step

        await user_path.save(using_db=conn)
        return skill_schema.UserPath(
            complited=user_path.current_step,
            current_module=user_path.current_module_code,
            lenght=user_path.path_len,
            path=[
                skill_schema.ModuleOut.model_validate(m)
                for m in user_path.path.get("path", [])
            ],
        )
