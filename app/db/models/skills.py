import typing
from tortoise import fields
from db.models import base

if typing.TYPE_CHECKING:
    from db.models import Resource


class ModulesInfo(base.BaseMixin, base.BaseModel):
    code = fields.CharField(max_length=128, unique=True)
    description = fields.TextField()
    level = fields.CharField(max_length=32)
    resources: fields.ManyToManyRelation["Resource"]

    class Meta:
        table = "modules_info"
