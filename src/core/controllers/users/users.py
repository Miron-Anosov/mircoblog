"""Users routes.

Routes:
    - POST /api/users/<id>/follow
    - GET /api/users/me
    - GET /api/users/<id>
    - POST api/users/new
"""

from typing import Annotated, Sequence

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer

from src.core.controllers.depends.auth.check_token import token_is_alive
from src.core.controllers.depends.users.get_me import get_me
from src.core.controllers.depends.users.get_user_by_id import get_user_by_id
from src.core.settings.const import MimeTypes
from src.core.settings.routes_path import UsersRoutes
from src.core.validators import StatusResponse, UserProfile


def create_user_route() -> APIRouter:
    """Create user's routes.

    Return:
            APIRouter
    """
    return APIRouter(
        tags=[UsersRoutes.TAG],
        prefix=UsersRoutes.PREFIX,
    )


users: APIRouter = create_user_route()
token_depend: Sequence[Depends] = [
    Depends(token_is_alive),
    Depends(HTTPBearer(auto_error=False)),
]


@users.post(
    path=UsersRoutes.USERS_FOLLOW_BY_ID,
    status_code=status.HTTP_201_CREATED,
    dependencies=token_depend,
)
async def follow_users(user_id: str) -> StatusResponse:
    """
    Follow a new user by ID.

    **Headers**:
    - Authorization: Bearer `access_token` (str): User key authentication.

    **Body**:
    - `user_id (int)`: The ID of the user following.

    """
    return StatusResponse()


@users.delete(
    path=UsersRoutes.USERS_FOLLOW_BY_ID,
    status_code=status.HTTP_200_OK,
    dependencies=token_depend,
)
async def follow_users_delete(user_id: str) -> StatusResponse:
    """
    Unfollow any user by ID.

    **Headers**:
     - Authorization: Bearer `access_token` (str): User key authentication.

    **Body**:
    - `user_id (int)`: The ID of the user following.

    """
    return StatusResponse()


@users.get(
    path=UsersRoutes.GET_ME,
    status_code=status.HTTP_200_OK,
    response_model=UserProfile,
)
async def get_user_me(
    user_profile: Annotated[UserProfile, Depends(get_me)]
) -> "JSONResponse":
    """
    Get user profile.

    **Headers**:
     - Authorization: Bearer `access_token` (str): User key authentication.

    """
    return JSONResponse(
        content=user_profile.model_dump(),
        status_code=status.HTTP_200_OK,
        media_type=MimeTypes.APPLICATION_JSON,
    )


@users.get(
    path=UsersRoutes.GET_BY_ID,
    status_code=status.HTTP_200_OK,
    response_model=UserProfile,
)
async def get_user_profile_by_id(
    user_profile: Annotated[UserProfile, Depends(get_user_by_id)]
):
    """
    Get user profile.

    **Headers**:
     - Authorization: Bearer `access_token` (str): User key authentication.

    """
    return JSONResponse(
        content=user_profile.model_dump(),
        status_code=status.HTTP_200_OK,
        media_type=MimeTypes.APPLICATION_JSON,
    )
