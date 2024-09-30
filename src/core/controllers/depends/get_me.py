"""Return User Profile."""

from typing import TYPE_CHECKING, Annotated

from fastapi import Depends

from src.core.controllers.depends.check_token import token_is_alive
from src.core.controllers.depends.connect_db import get_crud, get_session
from src.core.validators import User, UserMe, UserProfile

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from src.core.models_orm.crud import Crud


async def get_me(
    id_user: Annotated[str, Depends(token_is_alive)],
    session: Annotated["AsyncSession", Depends(get_session)],
    crud: Annotated["Crud", Depends(get_crud)],
) -> "UserProfile":
    """Return User's profile.

    Args:
        - id_user (str): user ID.
        - session (AsyncSession): db session.
        - crud (Crud): crud worker interface
    Returns:
        - UserProfile (pydantic model)
    """
    user_profile = await crud.users.get_me(
        id_user=id_user,
        session=session,
    )

    return UserProfile(result=True, user=serialize_user(user_profile))


def serialize_user(user) -> "UserMe":
    """Return pydantic model UserProfile."""
    return UserMe(
        id=str(user.id),
        name=user.name,
        followers=[
            User(id=str(follower.id), name=follower.name)
            for follower in user.followers
        ],
        following=[
            User(id=str(followed.id), name=followed.name)
            for followed in user.following
        ],
    )
