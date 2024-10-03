"""Creator users."""

from typing import TYPE_CHECKING

from fastapi import HTTPException, status

from src.core.controllers.depends.utils.hash_password import hash_pwd
from src.core.controllers.depends.utils.return_error import http_exception
from src.core.settings.const import MessageError, TypeEncoding

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
) -> bool | None:
    """Create user in db."""
    if password != password_control:
        # TODO: Add logger DEBUG
        raise http_exception(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            error_type=MessageError.TYPE_ERROR_INVALID_AUTH,
            error_message=MessageError.INVALID_EMAIL_OR_PWD,
        )

    email_exist: bool = await crud.auth_users.if_exist_email(
        email=email,
        session=session,
    )
    if email_exist:
        # TODO loger DEBUG
        raise http_exception(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            error_message=MessageError.EMAIL_ALREADY_EXIST,
            error_type=MessageError.INVALID_EMAIL_OR_PWD,
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
