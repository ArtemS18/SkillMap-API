import typing
from tortoise import fields
from db.models import base

if typing.TYPE_CHECKING:
    from db.models.progress import Progress

class User(base.BaseMixin, base.BaseModel):
    provider: str = fields.CharField(max_length=128, null=True)
    email: str = fields.CharField(max_length=128, unique=True)
    firstname: str = fields.CharField(max_length=128)
    lastname: str = fields.CharField(max_length=128)
    hashed_password: str = fields.CharField(max_length=128)
    email_verified: bool = fields.BooleanField(default=False)

    progress: fields.OneToOneRelation["Progress"] = fields.OneToOneField("server.Progress", "user")
    

    def __str__():
        return "user"

