from typing import Any
from urllib.parse import urlencode
from pydantic_schemas import oauth2_schema
from service import exception
from db.models.user import UserAuthProvider
from config import settings

import aiohttp
import jwt


REDIRECT_URI = "http://localhost:5173/login/oauth/google"


def get_oauth_url() -> str:
    base_url = "https://accounts.google.com/o/oauth2/v2/auth"
    params = {
        "access_type": "offline",
        "include_granted_scopes": "true",
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "client_id": settings.google_client_id,
        "scope": "openid profile email",
    }
    query = urlencode(params)

    return f"{base_url}?{query}"


async def oauth_callback(code: str) -> oauth2_schema.UserOAuthCredentials:
    url = "https://oauth2.googleapis.com/token"
    payload = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": settings.google_client_id,
        "client_secret": settings.google_client_secret,
    }

    async with aiohttp.ClientSession() as client:
        data = await client.post(url, data=payload)
        try:
            json_data = await data.json()
        except Exception as e:
            raise exception.BadRequest(e.__str__())
    print(json_data)
    payload = jwt.decode(
        json_data["id_token"],
        algorithms=["RS256"],
        options={"verify_signature": False},
        verify=False,
    )
    print(payload)
    return oauth2_schema.UserOAuthCredentials(
        **payload, provider=UserAuthProvider.google
    )
