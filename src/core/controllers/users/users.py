"""Users routes.

Routes:
    - POST /api/users/<id>/follow
    - GET /api/users/me
    - GET /api/users/<id>
    - POST api/users/new
"""

from typing import Annotated, Sequence

from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPBearer

from src.core.controllers.depends.auth.check_token import token_is_alive
from src.core.controllers.depends.users.followers import (
    del_follow,
    post_follow,
)
from src.core.controllers.depends.users.get_me import get_me
from src.core.controllers.depends.users.get_user_by_id import get_user_by_id
from src.core.settings.routes_path import UsersRoutes
from src.core.validators import StatusResponse, UserProfile


def create_user_route() -> APIRouter:
    """Create user's routes.

    Return:
        APIRouter: tags ["Users"], prefix: "/api"
    """
    return APIRouter(
        tags=[UsersRoutes.TAG],
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
async def follow_users(
    _: Annotated[bool, Depends(post_follow)]
) -> StatusResponse:
    """
    Follow a new user by ID.

    **Headers**:
    - Authorization: Bearer `access_token` (str): User key authentication.

    **Body**:
    - `user_id (str)`: The ID of the user following.

    """
    return StatusResponse()


@users.delete(
    path=UsersRoutes.USERS_FOLLOW_BY_ID,
    status_code=status.HTTP_200_OK,
    dependencies=token_depend,
)
async def follow_users_delete(
    _: Annotated[bool, Depends(del_follow)]
) -> StatusResponse:
    """
    Unfollow any user by ID.

    **Headers**:
     - Authorization: Bearer `access_token` (str): User key authentication.

    **Body**:
    - `user_id (str)`: The ID of the user following.

    """
    return StatusResponse()


@users.get(
    path=UsersRoutes.GET_ME,
    status_code=status.HTTP_200_OK,
    response_model=UserProfile,
    dependencies=token_depend,
)
async def get_user_me(
    user_profile: Annotated[UserProfile, Depends(get_me)]
) -> "UserProfile":
    """
    **Headers**.

    - Authorization: Bearer `access_token` (str): User key authentication.
    - If-None-Match: (str) ETag value for cache validation.

    **Response**:
    - A JSON object containing the user's profile data.

    **Response Fields**:
    - `result (bool)`: Indicates if the request was successful.
    - `user (dict)`: User profile object, containing the following fields:
        - `id (str)`: Unique identifier of the user.
        - `name (str)`: The user's name.
        - `followers (List[dict])`: A list of users following this user:
            - `id (str)`: Unique identifier of the follower.
            - `name (str)`: The follower's name.
        - `following (List[dict])`: A list of users this user is following:
            - `id (str)`: Unique identifier of the followed user.
            - `name (str)`: The followed user's name.

    **Notes**:
    - The `followers` field contains user data for those who follow the user.
    - The `following` field contains user data for those the user follows.
    """
    return user_profile


@users.get(
    path=UsersRoutes.GET_BY_ID,
    status_code=status.HTTP_200_OK,
    response_model=UserProfile,
    dependencies=token_depend,
)
async def get_user_profile_by_id(
    user_profile: Annotated[UserProfile, Depends(get_user_by_id)]
):
    """
    Get user profile by ID.

    **Headers**:
    - Authorization: Bearer `access_token` (str): User key authentication.
    - If-None-Match: (str) ETag value for cache validation.

    **Response**:
    - A JSON object containing the user's profile data.

    **Response Fields**:
    - `result (bool)`: Indicates if the request was successful.
    - `user (dict)`: User profile object, containing the following fields:
        - `id (str)`: Unique identifier of the user.
        - `name (str)`: The user's name.
        - `followers (List[dict])`: A list of users following this user:
            - `id (str)`: Unique identifier of the follower.
            - `name (str)`: The follower's name.
        - `following (List[dict])`: A list of users this user is following:
            - `id (str)`: Unique identifier of the followed user.
            - `name (str)`: The followed user's name.

    **Notes**:
    - The `followers` field contains user data for those who follow the user.
    - The `following` field contains user data for those the user follows.
    """
    return user_profile
