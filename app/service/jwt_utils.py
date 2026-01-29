from typing import Any, Literal
import jwt
import pydantic
from datetime import datetime, timedelta, timezone

from service.exception import BadJWTCredentials
from pydantic_schemas import jwt_schema
from config import settings


def create_token(
    data: dict[str, Any],
    _expire_at: timedelta = settings.jwt_access_expires_at,
    _expire_in: datetime | None = None,
):
    now = datetime.now(timezone.utc)
    expire_at = now + _expire_at

    base_payload = jwt_schema.JWTBaseClaims(
        **data,
        exp=expire_at if not _expire_in else _expire_in,
        iss="backend",
        iat=now,
    ).model_dump(exclude_unset=True)

    extra_payload = {k: v for k, v in data.items() if base_payload.get(k) is None}
    base_payload.update(extra_payload)
    token = jwt.encode(
        base_payload,
        key=settings.jwt_access_secret_key,
        algorithm=settings.jwt_access_algorithm,
    )
    return token


def verifi_token(token: str) -> jwt_schema.JWTBaseClaims:
    try:
        payload = jwt.decode(
            token,
            key=settings.jwt_access_secret_key,
            algorithms=[settings.jwt_access_algorithm],
        )
    except jwt.exceptions.InvalidTokenError:
        raise BadJWTCredentials

    try:
        claims = jwt_schema.JWTBaseClaims(**payload)

        return claims
    except pydantic.ValidationError:
        raise BadJWTCredentials


def verifi_token_typ(
    token: str, typ: Literal["access", "refresh"]
) -> jwt_schema.JWTBaseClaims:
    claims = verifi_token(token)
    if claims.typ != typ:
        raise BadJWTCredentials
    return claims
