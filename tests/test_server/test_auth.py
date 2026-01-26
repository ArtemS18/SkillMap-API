import asyncio
import pytest

from tests.test_server.utils import create_user
from tests.utils import AsyncClient

REG_ENDPOIT = "/api/auth/reg"
LOGIN_ENDPOIT = "/api/auth/login"


@pytest.mark.asyncio
async def test_register_ok(async_client: AsyncClient):
    test_user = create_user()
    resp = await async_client.post(REG_ENDPOIT, data=test_user.model_dump())
    assert resp.status_code in (200, 201)
    data: dict = resp.json()
    assert data.get("email") == test_user.email


@pytest.mark.asyncio
async def test_register_422(async_client: AsyncClient):
    wrong_data = {"email": "test", "wrong": "..."}
    resp = await async_client.post(REG_ENDPOIT, data=wrong_data)
    assert resp.status_code == 422


@pytest.mark.asyncio
async def test_register_409(async_client: AsyncClient):
    test_user = create_user()
    resp_1 = await async_client.post(REG_ENDPOIT, data=test_user.model_dump())
    assert resp_1.status_code in (200, 201)
    resp_2 = await async_client.post(REG_ENDPOIT, data=test_user.model_dump())
    assert resp_2.status_code == 409


@pytest.mark.asyncio
async def test_login_ok(async_client: AsyncClient):
    # register test user
    test_user = create_user()
    resp_1 = await async_client.post(REG_ENDPOIT, data=test_user.model_dump())
    assert resp_1.status_code in (200, 201)

    # autho test user
    login_form = {"username": test_user.email, "password": test_user.password}
    resp_2 = await async_client.post(LOGIN_ENDPOIT, data=login_form)
    assert resp_2.status_code in (200, 201)
    assert resp_2.json()["access_token"]


@pytest.mark.asyncio
async def test_login_404(async_client: AsyncClient):
    # register test user
    test_user = create_user()
    login_form = {"username": test_user.email, "password": test_user.password}
    resp_2 = await async_client.post(LOGIN_ENDPOIT, data=login_form)
    assert resp_2.status_code == 404


@pytest.mark.asyncio
async def test_login_401(async_client: AsyncClient):
    test_user = create_user()
    await async_client.post(REG_ENDPOIT, data=test_user.model_dump())

    login_form = {"username": test_user.email, "password": "wrong_pwd"}
    resp_2 = await async_client.post(LOGIN_ENDPOIT, data=login_form)
    assert resp_2.status_code == 401
