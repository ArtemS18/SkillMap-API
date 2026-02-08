from datetime import datetime, timezone
from logging import getLogger
import uuid
from tortoise.expressions import Q
from db.models.user import UserAuthProvider
from pydantic_schemas import oauth2_schema
from redis_client.client import get_client
from db import models
from tortoise.exceptions import IntegrityError
from tortoise.transactions import in_transaction
from pydantic_schemas import user_schema, auth_schema
from config import settings
from service import exception as service_exp, jwt_utils, pwd

DEFAULT_SCOPES = ["me", "roadmap.read", "roadmap.write"]

log = getLogger(__name__)


async def register(create: user_schema.CreateUser) -> user_schema.OutUser:
    _hashed_password = pwd.hash_password(create.password)
    try:
        user = await models.User.create(
            **create.model_dump(exclude=["password"]), hashed_password=_hashed_password
        )
        return user_schema.OutUser.model_validate(user)
    except IntegrityError:
        raise service_exp.AlreadyExist("user")


async def check_if_user_exist(email: str) -> bool:
    is_user_exists = await models.User.exists(email=email, email_verified=False)
    if not is_user_exists:
        raise service_exp.NotFoundError("user")
    redis = get_client()
    exits = await redis.get(f"verify-code:{email}")
    if exits:
        raise service_exp.AlreadyExist("verify code")
    return True


async def create_refresh_token_and_save(user_id: int, scopes: list[str]) -> str:
    now = datetime.now(timezone.utc)
    expire_at = now + settings.jwt_refresh_expires_at
    jti = str(uuid.uuid4())

    refresh_token = jwt_utils.create_token(
        {"sub": str(user_id), "scope": " ".join(scopes), "typ": "refresh", "jti": jti},
        _expire_in=expire_at,
    )
    await models.RefreshToken.create(id=jti, user_id=user_id, expire_at=expire_at)
    return refresh_token


async def login(username: str, password: str, scopes: list[str]) -> auth_schema.AuthOut:
    exist_user = await models.User.filter(
        Q(email=username) & Q(Q(provider=None) | Q(provider=UserAuthProvider.email))
    ).first()
    if exist_user is None:
        raise service_exp.NotFoundError("user")
    if not exist_user.email_verified:
        raise service_exp.BadRequest("email is not verified")
    if not pwd.verifi_password(password, exist_user.hashed_password):
        raise service_exp.BadCredentials

    access_expire = settings.jwt_access_expires_at

    access_token = jwt_utils.create_token(
        {"sub": str(exist_user.id), "scope": " ".join(scopes), "typ": "access"},
        access_expire,
    )
    refresh_token = await create_refresh_token_and_save(exist_user.id, scopes)

    return auth_schema.AuthOut(
        access_token=access_token,
        refresh_token=refresh_token,
        expire_in=access_expire.seconds,
        scopes=" ".join(scopes),
    )


async def refresh(refresh_token: str) -> auth_schema.AuthOut:
    payload = jwt_utils.verifi_token_typ(refresh_token, "refresh")
    async with in_transaction() as conn:
        cur_token = await models.RefreshToken.select_for_update(
            using_db=conn
        ).get_or_none(id=payload.jti, user_id=int(payload.sub))
        if cur_token is None:
            raise service_exp.BadJWTCredentials
        if cur_token.expire_at < datetime.now(timezone.utc):
            raise service_exp.BadJWTCredentials
        if cur_token.is_banned:
            raise service_exp.BadJWTCredentials
        cur_token.is_banned = True
        await cur_token.save(using_db=conn)

    refresh_token = await create_refresh_token_and_save(
        int(payload.sub), payload.scope.split(" ")
    )

    access_expire = settings.jwt_access_expires_at

    access_token = jwt_utils.create_token(
        {"sub": payload.sub, "scope": payload.scope, "typ": "access"},
        access_expire,
    )
    log.debug(payload)
    return auth_schema.AuthOut(
        access_token=access_token,
        refresh_token=refresh_token,
        expire_in=access_expire.seconds,
        scopes=payload.scope or "",
    )


async def create_or_get_user_oauth(cred: oauth2_schema.UserOAuthCredentials):
    user = await models.User.get_or_create(
        {
            "email": cred.email,
            "name": cred.name,
            "email_verified": cred.email_verified,
            "provider": cred.provider,
            "external_id": cred.sub,
        },
        external_id=cred.sub,
        provider=cred.provider,
    )
    return user[0]


async def login_by_oauth(
    cred: oauth2_schema.UserOAuthCredentials,
) -> auth_schema.AuthOut:
    user = await create_or_get_user_oauth(cred)

    access_expire = settings.jwt_access_expires_at

    access_token = jwt_utils.create_token(
        {"sub": str(user.id), "scope": " ".join(DEFAULT_SCOPES), "typ": "access"},
        access_expire,
    )
    refresh_token = await create_refresh_token_and_save(user.id, DEFAULT_SCOPES)

    return auth_schema.AuthOut(
        access_token=access_token,
        refresh_token=refresh_token,
        expire_in=access_expire.seconds,
        scopes=" ".join(DEFAULT_SCOPES),
    )
