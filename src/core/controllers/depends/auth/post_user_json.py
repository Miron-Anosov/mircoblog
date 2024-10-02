"""Depends for new users."""

from typing import TYPE_CHECKING, Annotated

from fastapi import Depends

from src.core.controllers.depends.auth.create_user import create_user
from src.core.controllers.depends.connect_db import get_crud, get_session
from src.core.settings.const import TypeEncoding
from src.core.validators import NewUser

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from src.core.models_orm.crud import Crud


async def user_json(
    new_user: NewUser,
    crud: Annotated["Crud", Depends(get_crud)],
    session: Annotated["AsyncSession", Depends(get_session)],
) -> bool:
    """Create a new user from form data.

    Args:
        new_user: NewUser
        crud: CRUD operations handler
        session: AsyncSession for database operations

    Returns:
        JSONResponse: Confirmation of user creation or error message

    Raises:
        HTTPException
    """
    created_user = create_user(
        name=new_user.name,
        email=new_user.email,
        password=new_user.password.decode(TypeEncoding.UTF8),
        password_control=new_user.password_control.decode(TypeEncoding.UTF8),
        crud=crud,
        session=session,
    )
    return True if created_user else False
