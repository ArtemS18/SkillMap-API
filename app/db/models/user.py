from tortoise import fields
from db.models import base

from db.models.path import UserPath
from db.models.progress import UserModuleProgress


class User(base.BaseMixin, base.BaseModel):
    provider: str = fields.CharField(max_length=128, null=True)
    email: str = fields.CharField(max_length=128, unique=True)
    firstname: str = fields.CharField(max_length=128)
    lastname: str = fields.CharField(max_length=128)
    hashed_password: str = fields.CharField(max_length=128)
    email_verified: bool = fields.BooleanField(default=False)
    have_active_path: bool = fields.BooleanField(default=False)

    modules: fields.BackwardFKRelation[list["UserModuleProgress"]]
    paths: fields.BackwardFKRelation[list["UserPath"]]

    def __str__(self):
        return "user"
