from typing import Generic, Optional, Type, TypeVar
from tortoise import models
from tortoise.exceptions import IntegrityError
from tortoise.contrib.pydantic import PydanticModel
from pydantic import BaseModel

from service.exception import BadRequest, NotFoundError

_TortoiseModel = TypeVar("TortoiseModel", bound=models.Model)
_GetSchema = TypeVar("GetSchema", bound=PydanticModel)
_UpdateSchema = TypeVar("UpdateSchema", bound=BaseModel)
_CreateSchema = TypeVar("CreateSchema", bound=BaseModel)


class CRUDService(Generic[_TortoiseModel, _GetSchema, _UpdateSchema, _CreateSchema]):
    model: Type[_TortoiseModel]
    create_schema: Type[_CreateSchema]
    update_schema: Type[_UpdateSchema]
    get_schema: Type[_GetSchema]

    async def create(self, _create_schema: _CreateSchema) -> Optional[_GetSchema]:
        try:
            obj = await self.model.create(**_create_schema.model_dump(exclude_unset=True))
            return await self.get_schema.from_tortoise_orm(obj)
        except IntegrityError:
            raise BadRequest
        
    
    async def get_s(self, **kwargs) ->Optional[_GetSchema]:
        obj = await self.model.filter(**kwargs).first()
        if not obj:
            raise NotFoundError(name=self.model.__str__())
        
        return await self.get_schema.from_tortoise_orm(obj)
    
    async def update(self, _update_schema:_UpdateSchema,  **kwargs):
        count = await self.model.filter(**kwargs).update(**_update_schema.model_dump(exclude_unset=True))
        if not count: 
            raise NotFoundError(name=self.model.__str__())

        return await self.get_schema.from_queryset_single(self.model.get(**kwargs))
    
    async def all(self, **kwargs) -> Optional[_GetSchema]:
        return await self.get_schema.from_queryset(self.model.filter(**kwargs).all())
    
    async def delete(self, **kwargs) -> None:
        count = await self.model.filter(**kwargs).delete()
        if not count: 
            raise NotFoundError(name=self.model.__str__())