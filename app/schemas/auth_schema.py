from pydantic import BaseModel


class UserCredentials(BaseModel):
    username: str
    password: str


class TokenOut(BaseModel):
    token_type: str = "bearer"
    access_token: str
    expire_in: int
