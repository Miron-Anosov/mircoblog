"""User routes."""

from typing import Annotated

from fastapi import APIRouter, Depends, status

from ..settings.routes_path import PathRoutes
from .controller_dependends.http_handler_api_key import api_key_depend

users = APIRouter(tags=["Users"], prefix=PathRoutes.PREFIX.value)


@users.post(
    path=PathRoutes.USERS_FOLLOW_BY_ID.value,
    status_code=status.HTTP_201_CREATED,
)
def follow_users(
    user_id: int,
    api_key: Annotated[str, Depends(api_key_depend)],
):
    """
    Follow a new user by ID.

    **Headers**:
    - `api_key (str)*`: API key for authentication.

    **Body**:
    - `user_id (int)`: The ID of the user following.

    """
    pass


@users.delete(
    path=PathRoutes.USERS_FOLLOW_BY_ID.value,
    status_code=status.HTTP_201_CREATED,
)
def follow_users_delete(
    user_id: int,
    api_key: Annotated[str, Depends(api_key_depend)],
):
    """
    Unfollow any user by ID.

    **Headers**:
    - `api_key (str)*`: API key for authentication.

    **Body**:
    - `user_id (int)`: The ID of the user following.

    """
    pass
