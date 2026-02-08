import json
from logging import getLogger
from typing import Any
from urllib.parse import urlencode
from pydantic_schemas import oauth2_schema
from service import exception
from db.models.user import UserAuthProvider
from config import settings
from jwt.algorithms import RSAAlgorithm

import aiohttp
import jwt


REDIRECT_URI = "http://skillmap.ddns.net:80/login/oauth/google"
JWT_PUBLIC_KEY_URI = "https://www.googleapis.com/oauth2/v3/certs"

log = getLogger(__name__)


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


async def _get_pub_key_by_kid(kid: str) -> dict[str, Any] | None:
    async with aiohttp.ClientSession() as client:
        data = await client.get(JWT_PUBLIC_KEY_URI)
        try:
            json_data: dict[str, Any] = await data.json()
        except Exception as e:
            raise exception.ServiceExeption(e.__str__())
        log.debug("json: %s, kid: %s", json_data, kid)
        keys = json_data["keys"]

    for k in keys:
        if k["kid"] == kid:
            return k
    return None


async def _get_user_credetials(id_token: str) -> dict[str, Any]:
    header = jwt.get_unverified_header(id_token)
    kid = header.get("kid")
    jwk_data = await _get_pub_key_by_kid(kid)
    if jwk_data is None:
        raise exception.BadRequest("jwk_data not found")
    log.debug(jwk_data)
    pub_key = RSAAlgorithm.from_jwk(jwk_data)
    payload = jwt.decode(
        id_token,
        pub_key,
        algorithms=["RS256"],
        audience=settings.google_client_id,
    )
    log.debug(payload)
    return payload


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
            json_data: dict[str, Any] = await data.json()
        except Exception as e:
            raise exception.BadRequest(e.__str__())
    token: str = json_data.get("id_token")
    if token is None:
        raise exception.BadRequest("id token not found")
    payload = await _get_user_credetials(token)
    return oauth2_schema.UserOAuthCredentials(
        **payload, provider=UserAuthProvider.google
    )
