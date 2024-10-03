"""Depends for new users."""

from typing import TYPE_CHECKING, Annotated

import pydantic
from fastapi import Depends, Form

from src.core.controllers.depends.auth.create_user import create_user
from src.core.controllers.depends.connect_db import get_crud, get_session

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from src.core.models_orm.crud import Crud


async def user_form(
    name: Annotated[
        str,
        Form(
            description="Author's name: English, digits and one underscore.",
            min_length=2,
            max_length=15,
            pattern=r"^[a-zA-Z0-9_]+$",
        ),
    ],
    email: Annotated[
        pydantic.EmailStr,
        Form(
            description="User's email.",
        ),
    ],
    password: Annotated[
        str,
        Form(
            min_length=8,
            max_length=64,
            description="User's secret.",
        ),
    ],
    password_control: Annotated[
        str,
        Form(
            min_length=8,
            max_length=64,
            description="User's secret for check both.",
        ),
    ],
    crud: Annotated["Crud", Depends(get_crud)],
    session: Annotated["AsyncSession", Depends(get_session)],
) -> bool:
    """Create a new user from form data.

    Args:
        name: User's name
        email: User's email address
        password: User's password
        password_control: Password confirmation
        crud: CRUD operations handler
        session: AsyncSession for database operations

    Returns:
        JSONResponse: Confirmation of user creation or error message

    Raises:
        HTTPException
    """
    created_user = await create_user(
        name=name,
        email=email,
        password=password,
        password_control=password_control,
        crud=crud,
        session=session,
    )
    return True if created_user else False
