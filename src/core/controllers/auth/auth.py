"""Auth routes.

Routes:
    - POST /api/auth/login
    - POST /api/auth/logout
    - POST /api/auth/users
"""

from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from src.core.controllers.depends.login_user import (
    login_user_form,
    login_user_json,
)
from src.core.controllers.depends.new_user_form import create_new_user_form
from src.core.controllers.depends.new_user_json import create_new_user_json
from src.core.settings.routes_path import AuthRoutes
from src.core.validators import StatusResponse, UserToken

# from fastapi.responses import RedirectResponse


def create_auth_route() -> APIRouter:
    """Create user's routes.

    Return:
    - APIRouter
    """
    return APIRouter(tags=[AuthRoutes.TAG], prefix=AuthRoutes.PREFIX)


auth: APIRouter = create_auth_route()


@auth.post(
    path=AuthRoutes.POST_CREATE_USER_FORM,
    status_code=status.HTTP_201_CREATED,
    response_model=StatusResponse,
)
async def new_user_form(
    _: Annotated[bool, Depends(create_new_user_form)]
) -> JSONResponse:
    """**Post new user**.

    **Body**:
    - `name` (str): user's name.
    - `password` (str): user's secret.
    - `password-control` (str): same user's secret control again.
    - `email` (str): personal email

    """
    return JSONResponse(
        content=StatusResponse().model_dump(),
        status_code=status.HTTP_201_CREATED,
        media_type="application/json",
    )


@auth.post(
    path=AuthRoutes.POST_CREATE_USER_JSON,
    status_code=status.HTTP_201_CREATED,
    response_model=StatusResponse,
)
async def new_user_json(
    _: Annotated[bool, Depends(create_new_user_json)]
) -> JSONResponse:
    """**Post new user**.

    **Body**:
    - `name` (str): user's name.
    - `password` (str): user's secret.
    - `password-control` (str): same user's secret control again.
    - `email` (str): personal email

    """
    return JSONResponse(
        content=StatusResponse().model_dump(),
        status_code=status.HTTP_201_CREATED,
        media_type="application/json",
    )


@auth.post(
    path=AuthRoutes.POST_LOGIN_USER_JSON,
    status_code=status.HTTP_200_OK,
    response_model=UserToken,
)
async def login_json(
    user_token: Annotated[UserToken, Depends(login_user_json)]
) -> "JSONResponse":
    """**Post loging user**.

    **Body**:
    - `name` (str): user's name.
    - `password` (str): user's secret.

    """
    # response.set_cookie(key="x-auth-token", value="test-token")

    return JSONResponse(
        content=user_token.model_dump(),
        status_code=status.HTTP_200_OK,
        media_type="application/json",
        headers={"x-auth-token": "TEST"},
    )


@auth.post(
    path=AuthRoutes.POST_LOGIN_USER_FORM,
    status_code=status.HTTP_200_OK,
    response_model=UserToken,
)
async def login_form(
    user_token: Annotated[UserToken, Depends(login_user_form)]
) -> "JSONResponse":
    """**Post loging user**.

    **Body**:
    - `name` (str): user's name.
    - `password` (str): user's secret.

    """
    # response.set_cookie(key="x-auth-token", value="test-token")

    return JSONResponse(
        content=user_token.model_dump(),
        status_code=status.HTTP_200_OK,
        media_type="application/json",
        headers={"x-auth-token": "TEST"},
    )
