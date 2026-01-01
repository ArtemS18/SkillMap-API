import jwt
import pydantic
from datetime import datetime, timedelta, timezone

from service.exception import BadJWTCredentials
from schemas import jwt_schema
from config import settings


def create_access_token(user_id: int, _expire_at: timedelta = settings.jwt_access_expires_at):
    now = datetime.now(timezone.utc)
    expire_at = now + _expire_at

    payload = jwt_schema.JWTBaseClaims(
        sub=str(user_id),
        scope=["access"],
        exp=expire_at,
        iss="backend",
        iat=now
    )
    token = jwt.encode(
        payload.model_dump(), 
        key=settings.jwt_access_secret_key, 
        algorithm=settings.jwt_access_algorithm
    )
    return token

def verifi_token(token: str) -> jwt_schema.JWTBaseClaims:
    try: 
        payload = jwt.decode(
            token,  
            key=settings.jwt_access_secret_key, 
            algorithms=[settings.jwt_access_algorithm]
        )
    except jwt.exceptions.InvalidTokenError:
        raise BadJWTCredentials
    
    try: 
        claims = jwt_schema.JWTBaseClaims(**payload)
        return claims
    except pydantic.ValidationError:
        raise BadJWTCredentials