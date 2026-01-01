from typing import Annotated
from fastapi import APIRouter, Form, Security
from schemas import user_schema, auth_schema
from service import auth
from depends import get_current_user_id

auth_router = APIRouter(prefix="/auth")

@auth_router.post("/reg")
async def register(create_form: Annotated[user_schema.CreateUser, Form()]) -> user_schema.OutUser:
    return await auth.register(create_form)


@auth_router.post("/login")
async def login(cred_form: Annotated[auth_schema.UserCredentials, Form()]) -> auth_schema.TokenOut:
    return await auth.login(cred_form)

@auth_router.get("/securety")
async def test(user_id = Security(get_current_user_id, scopes=["items"])):
    return {"ok": True, "user_id": user_id}