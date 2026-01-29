from tortoise import fields
from db.models.user import User
from db.models import base


class RefreshToken(base.TimeMixin, base.BaseModel):
    id = fields.CharField(max_length=257, primary_key=True)
    is_banned = fields.BooleanField(default=False)
    user: fields.ForeignKeyRelation["User"] = fields.ForeignKeyField("server.User")
    expire_at = fields.DatetimeField(null=True)

    class Meta:
        table = "refresh_tokens"
        unique_together = (("user", "id"),)
