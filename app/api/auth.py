from typing import Annotated
from fastapi import APIRouter, Depends, Form, status
from fastapi.security import OAuth2PasswordRequestForm
from schemas import user_schema, auth_schema
from service import auth

auth_router = APIRouter(prefix="/auth", tags=["Autho"])


@auth_router.post("/reg", status_code=status.HTTP_201_CREATED)
async def register(
    create_form: Annotated[user_schema.CreateUser, Form()],
) -> user_schema.OutUser:
    return await auth.register(create_form)


@auth_router.post("/login")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> auth_schema.TokenOut:
    return await auth.login(form_data)
