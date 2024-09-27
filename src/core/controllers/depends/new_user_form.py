"""Depends for new users."""

from typing import TYPE_CHECKING, Annotated

import pydantic
from fastapi import Depends, Form, HTTPException, status

from src.core.controllers.depends.connect_db import get_crud, get_session
from src.core.controllers.depends.hash_password import hash_pwd
from src.core.validators import ErrResp

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from src.core.models_orm.crud import Crud


async def create_new_user_form(
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
    if password != password_control:
        # TODO: Add logger DEBUG
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=ErrResp(
                error_type="ValidationError",
                error_message="password is invalid.",
            ).model_dump(),
        )

    email_exist: bool = await crud.auth_users.if_exist_email(
        email=email,
        session=session,
    )
    if email_exist:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="email already exist",
        )

    # TODO: HASH AND SOLT AND PAPER PASSWORD
    password_hash = hash_pwd(password)
    new_user = dict(
        name=name, hashed_password=password_hash.decode("utf-8"), email=email
    )

    created_user = await crud.auth_users.post_new_user(
        session=session, auth_user=new_user
    )
    return True if created_user else False
