"""Depends for new users."""

from typing import TYPE_CHECKING, Annotated

import pydantic
from fastapi import Depends, Form, HTTPException, status
from fastapi.responses import JSONResponse

from src.core.controllers.depends.connect_db import get_crud, get_session
from src.core.controllers.depends.utils.hash_password import validate_pwd
from src.core.controllers.depends.utils.jwt_token import create_token
from src.core.settings.const import JWT, MessageError, TypeEncoding
from src.core.validators import LoginUser, UserToken

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from src.core.models_orm.crud import Crud


async def login_user_json(
    validate_user: LoginUser,
    crud: Annotated["Crud", Depends(get_crud)],
    session: Annotated["AsyncSession", Depends(get_session)],
) -> "JSONResponse":
    """Check user in DB than create tokens.

    Args:
        validate_user: LoginUser()
        crud: Crud()
        session: AsyncSession
    Return:
        UserToken(access_token: str, token_type: str)
    Raises:
        HTTPException()
    Notes:
        Return new JWT access token and refresh token.
    """
    return await login_user(
        username=validate_user.user_email,
        password=validate_user.password.decode(TypeEncoding.UTF8),
        session=session,
        crud=crud,
    )


async def login_user_form(
    username: Annotated[
        pydantic.EmailStr,
        Form(
            description="User's email.",
        ),
    ],
    password: Annotated[
        str,
        Form(
            min_length=1,
            max_length=64,
            description="User's secret.",
        ),
    ],
    crud: Annotated["Crud", Depends(get_crud)],
    session: Annotated["AsyncSession", Depends(get_session)],
) -> "JSONResponse":
    """Check user in DB than create tokens.

    Args:
        username: str: user_email
        password: srt: secret
        crud: Crud()
        session: AsyncSession
    Return:
        UserToken(access_token: str, token_type: str)
    Raises:
        HTTPException()
    Notes:
        Return new JWT access token and refresh token.
    """
    return await login_user(
        username=username, password=password, session=session, crud=crud
    )


async def login_user(
    username: str,
    password: str,
    crud: "Crud",
    session: "AsyncSession",
) -> "JSONResponse":
    """Check user in DB than create tokens.

    Args:
        username: str: user_email
        password: srt: secret
        crud: Crud()
        session: AsyncSession
    Return:
        UserToken(access_token: str, token_type: str)
    Raises:
        HTTPException()
    Notes:
        Return new JWT access token and refresh token.
    """
    user_hash_pwd, user_id = await crud.auth_users.login_user(
        email=username, session=session
    )

    if user_hash_pwd and validate_pwd(
        password=password,
        hash_password=user_hash_pwd.encode(TypeEncoding.UTF8),
    ):
        # TODO ADD LOGER DEBUG : successful login

        user_profile = await crud.users.get_user(
            id_user=user_id,
            session=session,
        )

        payload = {
            JWT.PAYLOAD_SUB_KEY: str(user_profile.id),
            JWT.PAYLOAD_USERNAME_KEY: user_profile.name,
        }

        user_token = UserToken(
            access_token=create_token(
                payload=payload, type_token=JWT.TOKEN_TYPE_ACCESS
            ),
            refresh_token=create_token(
                payload=payload, type_token=JWT.TOKEN_TYPE_REFRESH
            ),
        )

        response = JSONResponse(
            content=user_token.model_dump(
                exclude={
                    JWT.TOKEN_TYPE_REFRESH,
                    JWT.DESCRIPTION_PYDANTIC_EXPIRE_REFRESH,
                }
            ),
            status_code=status.HTTP_201_CREATED,
            media_type="application/json",
            # headers={"x-auth-token": user_token.access_token},
        )
        response.set_cookie(
            key=JWT.TOKEN_TYPE_REFRESH,
            value=user_token.refresh_token,
            httponly=True,
            # secure=True,
            expires=user_token.expires_refresh,
        )

        return response

    # TODO ADD LOGER DEBUG : unsuccessful login
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=MessageError.INVALID_EMAIL_OR_PWD,
    )
