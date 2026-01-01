from datetime import datetime
from pydantic import BaseModel


class JWTBaseClaims(BaseModel):
    sub: str
    scope: list[str]
    exp: datetime 
    iss: str
    iat: datetime


