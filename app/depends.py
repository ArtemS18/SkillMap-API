from typing_extensions import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from service import jwt_utils, exception


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
    return user_claims.sub
