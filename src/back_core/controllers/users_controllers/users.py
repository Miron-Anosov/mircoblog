"""Users routes.

Routes:
    - POST /api/users/<id>/follow
    - GET /api/users/me
    - GET /api/users/<id>
"""

from typing import Annotated

from fastapi import APIRouter, Depends, status

from back_core.settings.routes_path import UsersRoutes
from back_core.validators import StatusResponse, User, UserProfile

from ..controller_depends.http_handler_api_key import api_key_depend


def create_user_route() -> APIRouter:
    """Create user's routes.

    Return:
        APIRouter
    """
    return APIRouter(tags=[UsersRoutes.TAG], prefix=UsersRoutes.PREFIX)


users: APIRouter = create_user_route()


@users.post(
    path=UsersRoutes.USERS_FOLLOW_BY_ID,
    status_code=status.HTTP_201_CREATED,
)
def follow_users(
    user_id: str,
    api_key: Annotated[str, Depends(api_key_depend)],
) -> StatusResponse:
    """
    Follow a new user by ID.

    **Headers**:
    - `api_key (str)*`: API key for authentication.

    **Body**:
    - `user_id (int)`: The ID of the user following.

    """
    pass


@users.delete(
    path=UsersRoutes.USERS_FOLLOW_BY_ID,
    status_code=status.HTTP_200_OK,
)
def follow_users_delete(
    user_id: str,
    api_key: Annotated[str, Depends(api_key_depend)],
) -> StatusResponse:
    """
    Unfollow any user by ID.

    **Headers**:
    - `api_key (str)*`: API key for authentication.

    **Body**:
    - `user_id (int)`: The ID of the user following.

    """
    return StatusResponse()


@users.get(
    path=UsersRoutes.GET,
    status_code=status.HTTP_200_OK,
)
def get_user_profile(
    api_key: Annotated[str, Depends(api_key_depend)],
) -> UserProfile:
    """
    Get user profile.

    **Headers**:
    - `api_key (str)*`: API key for authentication.

    """
    return UserProfile()
