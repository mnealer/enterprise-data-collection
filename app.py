from fastapi import FastAPI
import settings
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from tortoise.contrib.fastapi import RegisterTortoise
from auth.middleware import authentication_middleware
from auth.auth_views import auth_views
from auth.exceptions import AlreadyLoggedInException, NotLoggedInException, PermissionFailedException
from auth.exceptions import already_logged_in_handler, not_logged_in_handler, permission_failed_handler


# Database set-up
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # app startup
    async with RegisterTortoise(
        app,
        db_url=settings.db_url,
        modules=settings.db_modules,
        generate_schemas=True,
        add_exception_handlers=True,
    ):
        # db connected
        yield
        # app teardown

app = FastAPI(lifespan=lifespan)

# Middleware
app.middleware('http')(authentication_middleware)

# Exception handling
app.exception_handlers[NotLoggedInException] = not_logged_in_handler
app.exception_handlers[AlreadyLoggedInException] = already_logged_in_handler
app.exception_handlers[PermissionFailedException] = permission_failed_handler

# Project routers
app.include_router(auth_views)

app.mount("/static", StaticFiles(directory=settings.static_dir), name="static")