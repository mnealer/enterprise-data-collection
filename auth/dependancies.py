from auth.exceptions import NotLoggedInException, PermissionFailedException, AlreadyLoggedInException
from fastapi import Request, BackgroundTasks
import datetime
from settings import max_age
from models import Session


async def update_session_expiry(request: Request):
    session = await Session.get(token=request.session)
    session.expires_at = datetime.datetime.now() + datetime.timedelta(seconds=max_age)
    await session.save()
    await Session.filter(expires_at__lt=datetime.datetime.now()).delete()


async def already_logged_in(request: Request):
    if request.user.is_authenticated:
        raise AlreadyLoggedInException()
    return True


async def logged_in(request: Request, background_tasks: BackgroundTasks) -> bool:
    if not request.user.is_authenticated:
        raise NotLoggedInException()
    background_tasks.add_task(update_session_expiry, request)
    return True


async def admin_user(request: Request, background_tasks: BackgroundTasks) -> bool:
    if not request.user.is_authenticated:
        raise NotLoggedInException()
    if "admin" not in request.auth or "super" not in request.auth:
        raise PermissionFailedException("You need to be marked as an admin user to access this endpoint")
    background_tasks.add_task(update_session_expiry, request)
    return True


async def super_user(request: Request, background_tasks: BackgroundTasks) -> bool:
    if not request.user.is_authenticated:
        raise NotLoggedInException()
    if "super" not in request.auth:
        raise PermissionFailedException("You need to be marked as an admin user to access this endpoint")
    background_tasks.add_task(update_session_expiry, request)
    return True
