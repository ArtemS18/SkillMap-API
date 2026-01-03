import typing
from tortoise import fields
from tortoise.fields.base import OnDelete

from db import constants
from db.models import base

if typing.TYPE_CHECKING:
    from db.models.user import User
    from app.db.models.status import Status


class UserModuleProgress(base.BaseMixin, base.BaseModel):
    module_code = fields.CharField(max_length=128, index=True)
    user: fields.ForeignKeyRelation["User"] = fields.ForeignKeyField(
        "server.User", related_name="modules"
    )
    status: fields.ForeignKeyRelation["Status"] = fields.ForeignKeyField(
        "server.Status", on_delete=OnDelete.SET_DEFAULT, default=constants.IN_PROGRESS
    )

    class Meta:
        table = "user_module_progress"
        unique_together = (("user", "module_code"),)

    def __str__(self):
        return "user_module_progress"
