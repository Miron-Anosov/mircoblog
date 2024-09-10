"""Users routes."""

from typing import Annotated

from fastapi import APIRouter, Depends, status

from back_core.settings.routes_path import UsersRoutes
from back_core.validators.valid_tweet import ValidStatusResponse
from back_core.validators.valid_user import ValidateUserProfile, ValidUserModel

from ..controller_depends.http_handler_api_key import api_key_depend


def create_user_route() -> APIRouter:
    """Create user's routes."""
    return APIRouter(tags=[UsersRoutes.TAG], prefix=UsersRoutes.PREFIX)


users = create_user_route()


@users.post(
    path=UsersRoutes.USERS_FOLLOW_BY_ID,
    status_code=status.HTTP_201_CREATED,
)
def follow_users(
    user_id: str,
    api_key: Annotated[str, Depends(api_key_depend)],
) -> ValidUserModel:
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
) -> ValidStatusResponse:
    """
    Unfollow any user by ID.

    **Headers**:
    - `api_key (str)*`: API key for authentication.

    **Body**:
    - `user_id (int)`: The ID of the user following.

    """
    return ValidStatusResponse()


@users.get(
    path=UsersRoutes.GET,
    status_code=status.HTTP_200_OK,
)
def get_user_profile(
    api_key: Annotated[str, Depends(api_key_depend)],
) -> ValidateUserProfile:
    """
    Get user profile.

    **Headers**:
    - `api_key (str)*`: API key for authentication.

    """
    return ValidateUserProfile()
