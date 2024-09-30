"""Depends for new users."""

from typing import TYPE_CHECKING, Annotated

from fastapi import Depends, HTTPException, status

from src.core.controllers.depends.connect_db import get_crud, get_session
from src.core.controllers.depends.utils.hash_password import hash_pwd
from src.core.validators import ErrResp, NewUser

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from src.core.models_orm.crud import Crud


async def create_new_user_json(
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
    if new_user.password != new_user.password_control:
        # TODO: Add logger DEBUG
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=ErrResp(
                error_type="ValidationError",
                error_message="password is invalid.",
            ).model_dump(),
        )

    email_exist: bool = await crud.auth_users.if_exist_email(
        email=new_user.user_email,
        session=session,
    )
    if email_exist:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="email already exist",
        )

    # TODO: HASH AND SOLT AND PAPER PASSWORD
    new_user.password = hash_pwd(new_user.password.decode("utf-8"))
    user_data = dict(
        name=new_user.name,
        hashed_password=new_user.password.decode("utf-8"),
        email=new_user.user_email,
    )
    await crud.auth_users.post_new_user(session=session, auth_user=user_data)
    return True
