from enum import IntEnum
from tortoise import fields
from db.models import base

from db.models.path import UserPath
from db.models.progress import UserModuleProgress


class UserAuthProvider(IntEnum):
    email = 1
    google = 2


class User(base.BaseMixin, base.BaseModel):
    email: str = fields.CharField(max_length=128, unique=True)
    name: str = fields.CharField(max_length=128)
    hashed_password: str = fields.CharField(max_length=128, null=True)
    email_verified: bool = fields.BooleanField(default=False)
    have_active_path: bool = fields.BooleanField(default=False)
    provider: str = fields.IntEnumField(
        UserAuthProvider, default=UserAuthProvider.email, null=True
    )
    external_id: str = fields.CharField(max_length=255, null=True, unique=True)

    modules: fields.BackwardFKRelation[list["UserModuleProgress"]]
    paths: fields.BackwardFKRelation[list["UserPath"]]

    def __str__(self):
        return "user"
