from pathlib import Path
from typing import Annotated
from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from auth.dependancies import already_logged_in
from auth import authenticate


auth_views = APIRouter(prefix="/auth")


@auth_views.get("/", response_class=HTMLResponse, dependencies=[Depends(already_logged_in)])
async def login_page():
    return HTMLResponse(content=Path("templates/auth/login.html").read_text(), status_code=200)


@auth_views.post("/check", dependencies=[Depends(already_logged_in)])
async def login_check(request: Request, username: Annotated[str, Form()], password: Annotated[str, Form()]):
    if await authenticate(request, username, password):
        return RedirectResponse("/", status_code=302)
    else:
        return HTMLResponse(content=Path("templates/auth/login.html").read_text(), status_code=200)



