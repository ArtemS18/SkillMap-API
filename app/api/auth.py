from typing import Annotated
from fastapi import APIRouter, BackgroundTasks, Depends, Form, Query, status
from fastapi.responses import RedirectResponse, PlainTextResponse
from fastapi.security import OAuth2PasswordRequestForm
from pydantic_schemas import user_schema, auth_schema, oauth2_schema
from service import auth, email, google_oauth

auth_router = APIRouter(prefix="/auth", tags=["Autho"])


@auth_router.post("/reg", status_code=status.HTTP_201_CREATED)
async def register(
    create_form: Annotated[user_schema.CreateUser, Form()],
) -> user_schema.OutUser:
    return await auth.register(create_form)


@auth_router.post("/login")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> auth_schema.AuthOut:
    return await auth.login(form_data)


@auth_router.post("/refresh")
async def refresh_token(
    schema: auth_schema.RefreshTokenIn,
) -> auth_schema.AuthOut:
    return await auth.refresh(schema.refresh_token)


@auth_router.post("/send-verify-code", status_code=status.HTTP_204_NO_CONTENT)
async def send_verify_code(
    schema: auth_schema.EmailVerifyIn,
    back_task: BackgroundTasks,
):
    await auth.check_if_user_exist(schema.to_email)
    back_task.add_task(email.send_verify_code, schema.to_email)
    return


@auth_router.post("/verify-email", status_code=status.HTTP_204_NO_CONTENT)
async def verify_email(
    schema: auth_schema.CodeVerifyIn,
):
    await email.verify_email_code(schema.email, schema.code)
    return


@auth_router.get("/google", response_class=RedirectResponse)
async def google_oauth_handler():
    redirect_url = google_oauth.get_oauth_url()
    return RedirectResponse(redirect_url, status.HTTP_302_FOUND)


@auth_router.post("/google/callback", response_model=auth_schema.AuthOut)
async def google_oauth_callback(schema: oauth2_schema.OAuthIn):
    cred = await google_oauth.oauth_callback(schema.code)
    return await auth.login_by_oauth(cred)
