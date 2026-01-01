# from typing import Annotated
# from fastapi import APIRouter, Depends
# from service.user import UserService
# from schemas import user_schema

# async def get_user_service():
#     return UserService()

# UserServiceDep = Annotated[UserService, Depends(get_user_service)]


# user_router = APIRouter()

# @user_router.post("/", response_model=user_schema.OutUser)
# async def register_user_handler(user_form: user_schema.CreateUser, user_service: UserServiceDep):
#     return await user_service.create(user_form)

    
# @user_router.get("/{id_}", response_model=user_schema.OutUser)
# async def get_user_handler(id_: int, user_service: UserServiceDep):
#     return await user_service.get_s(id=id_)


# @user_router.delete("/{id_}")
# async def delete_user_handler(id_: int, user_service: UserServiceDep):
#     return await user_service.delete(id=id_)


# @user_router.put("/{id_}", response_model=user_schema.OutUser)
# async def update_user_handler(id_: int, update_form: user_schema.UpdateUser, user_service: UserServiceDep):
#     return await user_service.update(update_form, id=id_)
