"""Return User Profile by ID."""

from typing import TYPE_CHECKING, Annotated

from fastapi import Depends

from src.core.controllers.depends.utils.connect_db import get_crud, get_session
from src.core.controllers.depends.utils.serialize_user import serialize_user
from src.core.validators import UserProfile

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from src.core.models_orm.crud import Crud


async def get_user_by_id(
    id: str,  # noqa
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
    Notes:
        - Return profile without a token.
    """
    user_profile = await crud.users.get_me(
        id_user=id,
        session=session,
    )

    return UserProfile(result=True, user=serialize_user(user_profile))
