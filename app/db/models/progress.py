import typing
from tortoise import fields
from db.models import base

if typing.TYPE_CHECKING:
    from db.models.user import User

class Progress(base.BaseMixin, base.BaseModel):
    current_module: str = fields.CharField(max_length=128, null=True)
    module_skill_learned: int = fields.SmallIntField()
    module_progress: float = fields.FloatField()

    user: fields.BackwardOneToOneRelation["User"]

    def __str__():
        return "progress"

