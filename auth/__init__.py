from settings import max_age
from fastapi import Request
import datetime
import hashlib
from auth.models import Session, Users


class BaseUser:
    @property
    def is_authenticated(self) -> bool:
        raise NotImplementedError()


class UnauthenticatedUser(BaseUser):
    @property
    def is_authenticated(self) -> bool:
        return False


class AuthUser(BaseUser):
    def __init__(self, session: Session) -> None:
        self.session = session
        self.__user = None

    @property
    def is_authenticated(self) -> bool:
        return True

    async def user(self) -> Users:
        if not self.__user:
            self.__user = await Users.get_or_none(id=self.session.user)
        return self.__user


async def authenticate(request: Request, user: str, password: str) -> bool:
    user = await Users.get_or_none(username=user)
    if user:
        p_hash = hashlib.pbkdf2_hmac("sha256", password.encode(), user.p_salt, 100000)
        if p_hash == user.p_hash:
            expires = datetime.datetime.now() + datetime.timedelta(seconds=max_age)
            if await Session.filter(token=request.session).exists():
                await Session.filter(token=request.session).delete()
            session = await Session.create(user=user.id, expires_at=expires,
                                           scope=user.scope, token=request.session)
            request.scope["session"] = session.token
            request.scope["auth"] = user.scope
            auth_user = AuthUser(session)
            auth_user.__user = user
            request.scope["user"] = auth_user
            return True
        else:
            return False
    else:
        return False

