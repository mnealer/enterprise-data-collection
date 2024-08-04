from fastapi import Request
import random
from async_lru import alru_cache
from auth.models import Session, Users
from auth import AuthUser, UnauthenticatedUser
import settings


async def authentication_middleware(request: Request, call_next):
    token = request.cookies.get("session")
    if not token:
        request.scope["auth"] = ["anonymous"]
        request.scope["user"] = UnauthenticatedUser()
        request.scope['session'] = "".join(random.choices(settings.session_choices, k=128))
    else:
        @alru_cache(typed=True, maxsize=512, ttl=3600)
        async def get_session(token:str):
            return await Session.get_or_none(token=token)
        session = await get_session(request.scope['session'])
        if session is None:
            request.scope["auth"] = ["anonymous"]
            request.scope["user"] = UnauthenticatedUser()
        else:
            request.scope["user"] = AuthUser(session)
            @alru_cache(typed=True, maxsize=512, ttl=3600)
            async def get_user(user):
                return await Users.get_or_none(user=user)
            user = await get_user(session.user)
            request.scope["auth"] = user.scope
    response = await call_next(request)
    response.set_cookie("session", value=request.session, max_age=settings.max_age, httponly=True)
    return response
