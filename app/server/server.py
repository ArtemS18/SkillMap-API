from collections.abc import Callable
from contextlib import asynccontextmanager
from logging import getLogger
import time
from typing import AsyncGenerator, Awaitable
from fastapi.responses import JSONResponse
from tortoise import Tortoise, generate_config
from tortoise.contrib.fastapi import RegisterTortoise
from fastapi import FastAPI, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware

from logger import _init_logger
from redis_client import client as redis_client
from neo4j_client import client as neo4j_client
from gigachat.client import gigachat_client
from config import settings
from service import exception as service_exp

_init_logger()
log = getLogger(__name__)


async def add_process_time_header(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    log.info("%s %s: %.3f ms", request.method, request.url, process_time * 1000)
    return response


def _init_router(_app: FastAPI) -> None:
    from api import router

    _app.include_router(router)


def _init_middleware(_app: FastAPI) -> None:
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=settings.cors_allow_credentials,
        allow_methods=settings.cors_allow_methods,
        allow_headers=settings.cors_allow_headers,
    )
    _app.middleware("http")(add_process_time_header)


@asynccontextmanager
async def lifespan_test(_app: FastAPI) -> AsyncGenerator[None, None]:
    config = generate_config(
        db_url=settings.test_db_url,
        app_modules=settings.apps_for_tests,
        testing=True,
    )
    try:
        async with RegisterTortoise(
            app=_app,
            config=config,
            generate_schemas=True,
            add_exception_handlers=True,
            _create_db=True,
        ):
            await neo4j_client.connect(test_uri=settings.neo4j_test_url)
            yield
            await neo4j_client.disconnect()
            await redis_client.disconnect()
    except Exception:
        raise
    finally:
        await Tortoise._drop_databases()


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None, None]:
    try:
        if getattr(_app.state, "testing", None):
            async with lifespan_test(_app) as _:
                yield
        else:
            async with RegisterTortoise(
                app=_app,
                config=settings.tortoise_config,
                generate_schemas=True,
                add_exception_handlers=True,
            ):
                await neo4j_client.connect()
                await gigachat_client.connect()
                yield
                await neo4j_client.disconnect()
                await gigachat_client.disconnect()
                await redis_client.disconnect()
    except Exception:
        raise


def create_app() -> FastAPI:
    _app = FastAPI(
        title="Skill Map",
        description="Skill Map API",
        version="1.0.0",
        lifespan=lifespan,
        docs_url=settings.docs_url,
        redoc_url=settings.redoc_url,
    )
    _init_router(_app)
    _init_middleware(_app)

    return _app


app = create_app()


@app.exception_handler(service_exp.ServiceExeption)
async def validation_service_exp(req: Request, exption: service_exp.ServiceExeption):
    match type(exption):
        case service_exp.NotFoundError:
            _exption: service_exp.NotFoundError = exption
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"detail": f"{_exption.name.capitalize()} not found"},
            )
        case service_exp.BadRequest:
            _bad_req: service_exp.BadRequest = exption
            if _bad_req.detail is not None:
                return JSONResponse(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    content={"detail": _bad_req.detail},
                )
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"detail": "Bad request data"},
            )
        case service_exp.BadCredentials:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "Bad credentials"},
            )
        case service_exp.AlreadyExist:
            _exption: service_exp.AlreadyExist = exption
            return JSONResponse(
                status_code=status.HTTP_409_CONFLICT,
                content={"detail": f"{_exption.name.capitalize()} already exist"},
            )
