from typing import Annotated,Optional
from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from auth.dependancies import already_logged_in
from auth import authenticate
from admin.components import WebComponent


auth_views = APIRouter(prefix="/auth")


@auth_views.get("/login", response_class=HTMLResponse, dependencies=[Depends(already_logged_in)])
async def login_page(request: Request, next: Optional[str] = None):
    return HTMLResponse(WebComponent.render_template("templates/auth/login.html", next=next), status_code=200)


@auth_views.post("/login/check", dependencies=[Depends(already_logged_in)])
async def login_check(request: Request, username: Annotated[str, Form()], password: Annotated[str, Form()],
                      next: Optional[str] = None):
    if await authenticate(request, username, password):
        if next:
            return RedirectResponse(next)
        else:
            return RedirectResponse("/", status_code=302)
    else:
        if next:
            return RedirectResponse(f'/auth/login?next={next}', status_code=302)
        else:
            return RedirectResponse("/auth/login", status_code=302)



