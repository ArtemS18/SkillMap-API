from datetime import datetime
from tortoise import models, fields

class BaseModel(models.Model):
    pass 

class BaseMixin(BaseModel):
    id: int = fields.BigIntField(primary_key=True)
    created_at: datetime = fields.DatetimeField(auto_now_add=True, null=True)
    updated_at: datetime = fields.DatetimeField(auto_now=True, null=True)
