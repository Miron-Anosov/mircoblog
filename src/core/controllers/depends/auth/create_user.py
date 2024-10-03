"""Creater users."""

from typing import TYPE_CHECKING

from fastapi import HTTPException, status

from src.core.controllers.depends.utils.hash_password import hash_pwd
from src.core.settings.const import MessageError, TypeEncoding
from src.core.validators import ErrResp

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from src.core.models_orm.crud import Crud


async def create_user(
    name: str,
    email: str,
    password: str,
    password_control: str,
    crud: "Crud",
    session: "AsyncSession",
):
    """Create user in db."""
    if password != password_control:
        # TODO: Add logger DEBUG
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=ErrResp(
                error_type=MessageError.TYPE_ERROR_INVALID_AUTH,
                error_message=MessageError.INVALID_EMAIL_OR_PWD,
            ).model_dump(),
        )

    email_exist: bool = await crud.auth_users.if_exist_email(
        email=email,
        session=session,
    )
    if email_exist:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=MessageError.EMAIL_ALREADY_EXIST,
        )

    # TODO: HASH AND SOLT AND PAPER PASSWORD
    password_hash = hash_pwd(password)
    new_user = dict(
        name=name,
        hashed_password=password_hash.decode(TypeEncoding.UTF8),
        email=email,
    )

    return await crud.auth_users.post_new_user(
        session=session, auth_user=new_user
    )
