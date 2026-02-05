import typing
from tortoise import fields
from db.models import base

if typing.TYPE_CHECKING:
    from db.models import ModulesInfo


class Resource(base.BaseMixin, base.BaseModel):
    url = fields.CharField(max_length=256)
    title = fields.CharField(max_length=128)
    links: fields.BackwardFKRelation["ResourceModule"]

    class Meta:
        table = "resources"


class ResourceModule(base.BaseModel):
    resource = fields.ForeignKeyField(
        "server.Resource",
        "links",
        on_delete=fields.CASCADE,
    )
    module_code = fields.CharField(max_length=64)  # FIXME: add reference constains

    class Meta:
        table = "resources_modules_info"
        unique_together = ("resource", "module_code")
