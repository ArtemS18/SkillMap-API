from tortoise import fields
from db.models import base


class Status(base.BaseModel):
    id: int = fields.SmallIntField(primary_key=True)
    name = fields.CharField(max_length=32)


IN_PROGRESS = 1
CLOSED = 2
