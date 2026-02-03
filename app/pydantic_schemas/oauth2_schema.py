from pydantic import BaseModel
from db.models.user import UserAuthProvider


class UserOAuthCredentials(BaseModel):
    sub: str
    picture: str | None = None
    email: str
    email_verified: bool
    name: str
    provider: UserAuthProvider


class OAuthIn(BaseModel):
    code: str
