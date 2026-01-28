import typing
from tortoise import fields
from tortoise.contrib.postgres.indexes import GinIndex

from db import constants
from db.models.base import BaseMixin, BaseModel

if typing.TYPE_CHECKING:
    from db.models.user import User
    from db.models.status import Status


class UserPath(BaseMixin, BaseModel):
    user: fields.ForeignKeyRelation["User"] = fields.ForeignKeyField(
        "server.User", related_name="paths"
    )
    path: dict[str, str] = fields.JSONField()
    path_hash = fields.CharField(max_length=257, index=True)
    status: fields.ForeignKeyRelation["Status"] = fields.ForeignKeyField(
        "server.Status", on_delete=fields.SET_DEFAULT, default=constants.IN_PROGRESS
    )
    path_len = fields.IntField()
    current_module_code = fields.CharField(max_length=128, index=True)
    current_step = fields.IntField(default=0)

    class Meta:
        indexes = [GinIndex(fields=["path"], name="idx_user_path_gin")]
        # unique_together = (("user_id", "path_hash"),)
