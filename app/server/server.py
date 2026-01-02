from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi.responses import JSONResponse
from tortoise import Tortoise, generate_config
from tortoise.contrib.fastapi import RegisterTortoise
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from service import exception as service_exp


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
            yield
    except Exception as e:
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
                yield
    except Exception as e:
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
