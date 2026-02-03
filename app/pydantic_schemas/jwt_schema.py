from datetime import datetime
from pydantic import BaseModel, ConfigDict


class JWTBaseClaims(BaseModel):
    jti: str | None = None
    typ: str
    sub: str
    scope: str | None = None
    exp: datetime
    iss: str
    iat: datetime

    model_config = ConfigDict(extra="ignore")
