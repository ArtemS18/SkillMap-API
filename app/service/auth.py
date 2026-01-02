from fastapi.security import OAuth2PasswordRequestForm
from db import models
from tortoise.exceptions import IntegrityError
from schemas import user_schema, auth_schema
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


async def login(cred: OAuth2PasswordRequestForm) -> auth_schema.TokenOut:
    exist_user = await models.User.get_or_none(email=cred.username)
    if exist_user is None:
        raise service_exp.NotFoundError(f"user with email = {cred.username}")
    if not pwd.verifi_password(cred.password, exist_user.hashed_password):
        raise service_exp.BadCredentials
    access_expire = settings.jwt_access_expires_at
    token = jwt_utils.create_access_token(
        {"sub": str(exist_user.id), "scope": cred.scopes}, access_expire
    )
    return auth_schema.TokenOut(access_token=token, expire_in=access_expire.seconds)
