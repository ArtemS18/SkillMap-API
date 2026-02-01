from datetime import datetime, timezone
import uuid
from fastapi.security import OAuth2PasswordRequestForm
from redis_client.client import get_client
from db import models
from tortoise.exceptions import IntegrityError
from tortoise.transactions import in_transaction
from pydantic_schemas import user_schema, auth_schema
from config import settings
from service import exception as service_exp, jwt_utils, pwd


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
        {"sub": str(user_id), "scope": scopes, "typ": "refresh", "jti": jti},
        _expire_in=expire_at,
    )
    await models.RefreshToken.create(id=jti, user_id=user_id, expire_at=expire_at)
    return refresh_token


async def login(cred: OAuth2PasswordRequestForm) -> auth_schema.AuthOut:
    exist_user = await models.User.get_or_none(email=cred.username)
    if exist_user is None:
        raise service_exp.NotFoundError(f"user with email = {cred.username}")
    if not pwd.verifi_password(cred.password, exist_user.hashed_password):
        raise service_exp.BadCredentials

    access_expire = settings.jwt_access_expires_at

    access_token = jwt_utils.create_token(
        {"sub": str(exist_user.id), "scope": cred.scopes, "typ": "access"},
        access_expire,
    )
    refresh_token = await create_refresh_token_and_save(exist_user.id, cred.scopes)

    return auth_schema.AuthOut(
        access_token=access_token,
        refresh_token=refresh_token,
        expire_in=access_expire.seconds,
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

    refresh_token = await create_refresh_token_and_save(int(payload.sub), payload.scope)

    access_expire = settings.jwt_access_expires_at

    access_token = jwt_utils.create_token(
        {"sub": payload.sub, "scope": payload.scope, "typ": "access"},
        access_expire,
    )

    return auth_schema.AuthOut(
        access_token=access_token,
        refresh_token=refresh_token,
        expire_in=access_expire.seconds,
    )
