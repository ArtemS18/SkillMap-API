import asyncio
from app.db.models.status import IN_PROGRESS
from db.models import UserPath, User
from service import roadmap, exception
from hashlib import sha256
from schemas import skill_schema
from tortoise.exceptions import IntegrityError
from tortoise.transactions import in_transaction


async def create_user_path(
    user_id: int, target_skills: list[str]
) -> skill_schema.ModulePath:
    path = await roadmap.get_roadmap([], target_skills)
    hash_object = sha256(path.model_dump_json().encode())
    path_hash = hash_object.hexdigest()

    async with in_transaction() as conn:
        user = await User.select_for_update(using_db=conn).get_or_none(id=user_id)
        if user is None:
            raise exception.NotFoundError("user")
        if user.have_active_path:
            raise exception.AlreadyExist("active roadmap")

        current_module_code = None
        if path and path.path:
            current_module_code = path.path[0].id

        try:
            await UserPath.create(
                using_db=conn,
                user_id=user_id,
                path=path.model_dump(),
                path_hash=path_hash,
                current_module_code=current_module_code,
            )
        except IntegrityError:
            raise exception.AlreadyExist("path")

        user.have_active_path = True
        await user.save(update_fields=["have_active_path"], using_db=conn)

        return path


async def get_current_user_path(user_id: int) -> skill_schema.ModulePath:
    user_path = await UserPath.get_or_none(user_id=user_id, status=IN_PROGRESS)
    if user_path is None:
        raise exception.NotFoundError("active user path")
    return skill_schema.ModulePath.model_validate(user_path.path)
