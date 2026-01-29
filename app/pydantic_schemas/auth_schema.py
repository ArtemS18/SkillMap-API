from pydantic import BaseModel

from app.db.models import refresh


class UserCredentials(BaseModel):
    username: str
    password: str


class AccessTokenOut(BaseModel):
    token_type: str = "bearer"
    access_token: str
    expire_in: int


class RefreshTokenIn(BaseModel):
    refresh_token: str


class RefreshTokenOut(BaseModel):
    refresh_token: str


class AuthOut(AccessTokenOut, RefreshTokenOut): ...
