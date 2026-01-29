from datetime import datetime
from pydantic import BaseModel, ConfigDict


class JWTBaseClaims(BaseModel):
    jti: str | None = None
    typ: str
    sub: str
    scope: list[str | None] = []
    exp: datetime
    iss: str
    iat: datetime

    model_config = ConfigDict(extra="ignore")
