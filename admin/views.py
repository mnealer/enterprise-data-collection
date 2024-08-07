from pathlib import Path
from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from auth.dependancies import logged_in, admin_user


main_views = APIRouter()


@main_views.get("/admin", response_class=HTMLResponse, dependencies=[Depends(logged_in)])
def main_page(request: Request) -> HTMLResponse:
    return HTMLResponse(content=Path("templates/main.html").read_text(), status_code=200)



# login page

# main page

# table view

# detail view

# edit view

# create view

