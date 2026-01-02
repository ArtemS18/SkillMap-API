from datetime import datetime
from db import models
from tortoise.contrib.pydantic import pydantic_model_creator

_BaseUser = pydantic_model_creator(
    models.User,
    name="BaseUser",
    include=["email", "firstname", "lastname"],
    exclude_readonly=True,
)


class CreateUser(_BaseUser):
    password: str


class OutUser(_BaseUser):
    id: int
    created_at: datetime
    updated_at: datetime


_OptionalUser = pydantic_model_creator(
    models.User,
    name="UpdateUser",
    exclude=["hashed_password"],
    exclude_readonly=True,
    optional=tuple(models.User._meta.fields_map.keys()),
)


class UpdateUser(_OptionalUser): ...
