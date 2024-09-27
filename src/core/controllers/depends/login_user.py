"""Depends for new users."""

from typing import TYPE_CHECKING, Annotated

from fastapi import Depends, HTTPException, status

from src.core.controllers.depends.connect_db import get_crud, get_session
from src.core.controllers.depends.hash_password import validate_pwd
from src.core.controllers.depends.jwt_token import encode_jwt
from src.core.validators import LoginUser, UserToken

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from src.core.models_orm.crud import Crud


async def login_user_json(
    validate_user: LoginUser,
    crud: Annotated["Crud", Depends(get_crud)],
    session: Annotated["AsyncSession", Depends(get_session)],
) -> "UserToken":
    """Check user in DB.

    Args:
        validate_user: LoginUser()
        crud: Crud()
        session: AsyncSession
    Return:
        UserToken(access_token: str, token_type: str)
    Raises:
        HTTPException()
    Notes:
        Return new JWT token.
    """
    user_hash_pwd, user_id = await crud.auth_users.login_user(
        email=validate_user.user_email, session=session
    )

    if user_hash_pwd and validate_pwd(
        password=validate_user.password.decode("utf-8"),
        hash_password=user_hash_pwd.encode("utf-8"),
    ):
        # TODO ADD LOGER DEBUG

        user_profile = await crud.users.get_user(
            id_user=user_id,
            session=session,
        )

        payload = {
            "sub": user_profile.name,
            "username": user_profile.name,
        }

        new_token = encode_jwt(payload=payload)

        return UserToken(access_token=new_token)

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid email or password",
    )
