from typing_extensions import Annotated
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from service import jwt_utils, exception
from redis_client import client
import redis


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/auth/login",
    scheme_name="Access token",
    scopes={
        "me": "Read information about the current user.",
        "roadmap.read": "Read roadmap.",
        "roadmap.write": "Create roadmap.",
    },
)


def get_current_user_id(
    security_scopes: SecurityScopes, token: Annotated[str, Depends(oauth2_scheme)]
) -> int:
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = "Bearer"
    try:
        user_claims = jwt_utils.verifi_token(token)
    except exception.BadJWTCredentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token",
            headers={"WWW-Authenticate": authenticate_value},
        )

    for scope in security_scopes.scopes:
        if scope not in user_claims.scope:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value},
            )
    return int(user_claims.sub)


def request_limit(req_per_sec: int = 10):
    async def wrapper(req: Request):
        client_ip = req.client.host
        r = client.get_client()
        key = f"req_limit:{client_ip}"
        try:
            await r.watch(key)
            raw = await r.get(key)
            if not raw:
                await r.setex(key, 1, 1)
                return
            req_count = int(raw)
            print(req_count)
            if req_count + 1 > req_per_sec:
                await r.setex(key, 5, req_count + 1)
                await r.unwatch()
                raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS)
            else:
                await r.setex(key, 1, req_count + 1)
            await r.unwatch()
        except redis.WatchError:
            raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS)

    return wrapper
