"""Depends for new users."""

from typing import TYPE_CHECKING, Annotated

from fastapi import Depends, HTTPException, status

from src.core.controllers.depends.connect_db import get_crud, get_session
from src.core.validators import NewUser

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from src.core.models_orm.crud import Crud


async def valid_new_user(
    new_user: NewUser,
    crud: Annotated["Crud", Depends(get_crud)],
    session: Annotated["AsyncSession", Depends(get_session)],
) -> bool:
    """Check user in DB.

    new_user: UsersRoutes
    session: AsyncSession
    Return:
        - True: if user is already exists .
        - False: if user is not exist.
    """
    if new_user.password != new_user.password:
        # TODO: Add logger DEBUG
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="password is not same.",
        )

        # TODO: HASH AND SOLT AND PAPER PASSWORD

    result = await crud.auth_users.post_new_user(
        session=session, new_user=new_user.model_dump()
    )
    return result
