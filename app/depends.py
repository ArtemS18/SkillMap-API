from typing_extensions import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from service import jwt_utils, exception


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login", scheme_name="Access token")

def get_current_user_id(token: Annotated[str, Depends(oauth2_scheme)]) -> int:
    try:
        user_claims = jwt_utils.verifi_token(token)
    except exception.BadJWTCredentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token"
        )
    return user_claims.sub
    
