"""Auth routes.

Routes:
    - POST /api/auth/login
    - POST /api/auth/logout
    - POST /api/auth/users
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.responses import JSONResponse

from src.core.controllers.depends.new_user import valid_new_user
from src.core.controllers.depends.validate_user import login_user
from src.core.settings.routes_path import AuthRoutes
from src.core.validators import StatusResponse

# from fastapi.responses import RedirectResponse


def create_auth_route() -> APIRouter:
    """Create user's routes.

    Return:
    - APIRouter
    """
    return APIRouter(tags=[AuthRoutes.TAG], prefix=AuthRoutes.PREFIX)


auth: APIRouter = create_auth_route()


@auth.post(
    path=AuthRoutes.POST_CREATE_USER,
    status_code=status.HTTP_201_CREATED,
    response_model=StatusResponse,
)
async def new_user(
    user: Annotated[bool, Depends(valid_new_user)]
) -> StatusResponse:
    """**Post new user**.

    **Body**:
    - `name` (str): user's name.
    - `password` (str): user's secret.
    - `password-control` (str): same user's secret control again.
    - `email` (str): personal email

    """
    if user:
        return StatusResponse()
    return StatusResponse(result=user)


@auth.post(
    path=AuthRoutes.POST_LOGIN_USER,
    status_code=status.HTTP_200_OK,
    response_model=StatusResponse,
)
async def login(
    response: Response, user: Annotated[bool, Depends(login_user)]
) -> "JSONResponse":
    """**Post loging user**.

    **Body**:
    - `name` (str): user's name.
    - `password` (str): user's secret.

    """
    if user:
        response.set_cookie(key="x-auth-token", value="test-token")

        return JSONResponse(
            content=StatusResponse(),
            status_code=200,
            media_type="application/json",
            headers={"x-auth-token": "TEST"},
        )
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid email or password",
    )
