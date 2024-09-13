"""Users routes.

Routes:
    - POST /api/users/<id>/follow
    - GET /api/users/me
    - GET /api/users/<id>
"""

from typing import Sequence

from fastapi import APIRouter, Depends, status

from src.back_core.settings.routes_path import UsersRoutes
from src.back_core.validators import StatusResponse, UserProfile

from ..controller_depends.http_handler_api_key import api_key_depend


def create_user_route() -> APIRouter:
    """Create user's routes.

    Return:
        APIRouter
    """
    return APIRouter(tags=[UsersRoutes.TAG], prefix=UsersRoutes.PREFIX)


users: APIRouter = create_user_route()
api_key: Sequence[Depends] = [Depends(api_key_depend)]


@users.post(
    path=UsersRoutes.USERS_FOLLOW_BY_ID,
    status_code=status.HTTP_201_CREATED,
    dependencies=api_key,
)
def follow_users(user_id: str) -> StatusResponse:
    """
    Follow a new user by ID.

    **Headers**:
    - `api_key (str)*`: API key for authentication.
    Min length 6. Max length 60.

    **Body**:
    - `user_id (int)`: The ID of the user following.

    """
    pass


@users.delete(
    path=UsersRoutes.USERS_FOLLOW_BY_ID,
    status_code=status.HTTP_200_OK,
    dependencies=api_key,
)
def follow_users_delete(user_id: str) -> StatusResponse:
    """
    Unfollow any user by ID.

    **Headers**:
    - `api_key (str)*`: API key for authentication.
    Min length 6. Max length 60.

    **Body**:
    - `user_id (int)`: The ID of the user following.

    """
    return StatusResponse()


@users.get(
    path=UsersRoutes.GET_ME,
    status_code=status.HTTP_200_OK,
    response_model=UserProfile,
    dependencies=api_key,
)
def get_user_profile():
    """
    Get user profile.

    **Headers**:
    - `api_key (str)*`: API key for authentication.
    Min length 6. Max length 60.

    """
    return {"result": "Ok"}


@users.get(
    path=UsersRoutes.GET_BY_ID,
    status_code=status.HTTP_200_OK,
    dependencies=api_key,
    response_model=UserProfile,
)
def get_user_profile_by_id():
    """
    Get user profile.

    **Headers**:
    - `api_key (str)*`: API key for authentication.
     Min length 6. Max length 60.

    """
    ...
