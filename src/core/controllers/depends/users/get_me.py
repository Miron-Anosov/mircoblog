"""Return User Profile."""

from typing import TYPE_CHECKING, Annotated

from fastapi import Depends

from src.core.controllers.depends.auth.check_token import (
    get_user_id_by_token_access,
)
from src.core.controllers.depends.utils.connect_db import get_crud, get_session
from src.core.controllers.depends.utils.serialize_user import serialize_user
from src.core.validators import UserProfile

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from src.core.models_orm.crud import Crud


async def get_me(
    id_user: Annotated[str, Depends(get_user_id_by_token_access)],
    session: Annotated["AsyncSession", Depends(get_session)],
    crud: Annotated["Crud", Depends(get_crud)],
) -> "UserProfile":
    """Return User's profile.

    Args:
        id_user: str: user ID.
        session: AsyncSession: db session.
        crud: Crud: crud worker interface
    Returns:
        pydantic.BaseModel:UserProfile
    Notes:
        Return profile only with a token.
    """
    user_profile = await crud.users.get_me(
        id_user=id_user,
        session=session,
    )

    return UserProfile(result=True, user=serialize_user(user_profile))
