from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi import Request
"""
Authentication custom exceptions and exception handlers
"""


class NotLoggedInException(Exception):
    def __init__(self, request):
        pass


class AlreadyLoggedInException(Exception):
    def __init__(self):
        pass


class PermissionFailedException(Exception):
    def __init__(self, permissions: list):
        self.permissions = permissions



def already_logged_in_handler(request: Request, exc: AlreadyLoggedInException):
    return RedirectResponse("/")


def not_logged_in_handler(request: Request, exc: NotLoggedInException):
    """Redirect to the login page if login is required"""
    return RedirectResponse(f"/auth?next={request.url}")


def permission_failed_handler(request: Request, exc: PermissionFailedException):
    """shows an error page if the users authentication scope fails to meet the requirements"""
    return HTMLResponse(content="templates/permission_failed.html", status_code=401)

