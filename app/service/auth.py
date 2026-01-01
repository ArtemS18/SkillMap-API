from db import models
from tortoise.exceptions import IntegrityError
from schemas import user_schema, auth_schema
from config import settings
from service import exception as service_exp, jwt_utils, pwd



async def register(create: user_schema.CreateUser) -> user_schema.OutUser:
    _hashed_password = pwd.hash_password(create.password)
    try: 
        user = await models.User.create(
            **create.model_dump(exclude=["password"]), 
            hashed_password=_hashed_password
        )
        return user_schema.OutUser.model_validate(user)
    except IntegrityError:
        raise service_exp.AlreadyExist("user")
    
async def login(cred: auth_schema.UserCredentials) -> auth_schema.TokenOut:
    exist_user = await models.User.get_or_none(email=cred.username)
    if exist_user is None:
        raise service_exp.NotFoundError(f"user with email = {cred.username}")
    if not pwd.verifi_password(cred.password, exist_user.hashed_password):
        raise service_exp.BadCredentials
    token = jwt_utils.create_access_token(exist_user.id)
    return auth_schema.TokenOut(
        access_token=token, 
        expire_in=settings.jwt_access_expires_at.seconds
    )

    
    



    
    

