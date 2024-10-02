"""Auth routes.

Routes:
    - POST /api/auth/login
    - POST /api/auth/logout
    - POST /api/auth/users
    - DELETE /api/auth/logout
"""

from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.security import APIKeyCookie, HTTPBearer

from src.core.controllers.depends.auth.check_token import up_tokens_by_refresh
from src.core.controllers.depends.auth.login_user import (
    login_user_form,
    login_user_json,
)
from src.core.controllers.depends.auth.post_user_form import user_form
from src.core.controllers.depends.auth.post_user_json import user_json
from src.core.settings.const import JWT, Headers
from src.core.settings.routes_path import AuthRoutes
from src.core.validators import StatusResponse, UserToken


def create_auth_route() -> APIRouter:
    """Create user's routes.

    Return:
    - APIRouter
    """
    return APIRouter(
        tags=[AuthRoutes.TAG],
        prefix=AuthRoutes.PREFIX,
    )


auth: APIRouter = create_auth_route()


@auth.post(
    path=AuthRoutes.POST_CREATE_USER_FORM,
    status_code=status.HTTP_201_CREATED,
    response_model=StatusResponse,
)
async def new_user_form(
    _: Annotated[bool, Depends(user_form)]
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
    _: Annotated[bool, Depends(user_json)]
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
    status_code=status.HTTP_201_CREATED,
    response_model=UserToken,
)
async def login_json(
    user_token: Annotated["JSONResponse", Depends(login_user_json)],
) -> "JSONResponse":
    """**Post loging user**.

    **Body**:
    - `name` (str): user's name.
    - `password` (str): user's secret.

    Set Cookie:  `refresh_token`
    """
    return user_token


@auth.post(
    path=AuthRoutes.POST_LOGIN_USER_FORM,
    status_code=status.HTTP_201_CREATED,
    response_model=UserToken,
)
async def login_form(
    users_tokens: Annotated["JSONResponse", Depends(login_user_form)],
) -> "JSONResponse":
    """**Post loging user**.

    **Body**:
    - `name` (str): user's name.
    - `password` (str): user's secret.

    Set Cookie:  `refresh_token`
    """
    return users_tokens


@auth.patch(
    path=AuthRoutes.PATCH_TOKENS,
    status_code=status.HTTP_201_CREATED,
    response_model=UserToken,
)
async def patch_access_token(
    refresh_token: Annotated["JSONResponse", Depends(up_tokens_by_refresh)]
) -> "JSONResponse":
    """**Path access and refresh token**.

    Requirement :
        - Cookie:  `refresh_token`
    """
    return refresh_token


@auth.delete(
    path=AuthRoutes.DEL_LOGOUT_USER,
    status_code=status.HTTP_200_OK,
    response_model=StatusResponse,
    dependencies=[
        Depends(HTTPBearer()),
        Depends(APIKeyCookie(name=JWT.TOKEN_TYPE_REFRESH)),
    ],
)
async def logout_user() -> "JSONResponse":
    """**Delete loging user**.

    Requirement :
        - Cookie:  `refresh_token`
        - Authorization: Bearer

    """
    response = JSONResponse(
        content=StatusResponse().model_dump(),
        status_code=status.HTTP_200_OK,
    )
    response.delete_cookie(key=JWT.TOKEN_TYPE_REFRESH)
    response.headers.update(Headers.WWW_AUTH_BEARER_LOGOUT)
    response.headers.update(Headers.AUTHORIZATION)
    return response
