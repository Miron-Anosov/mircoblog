"""Depends-Check active user."""

from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError

from src.core.controllers.depends.utils.jwt_token import decode_jwt
from src.core.settings.const import JWT, Headers, MessageError
from src.core.settings.routes_path import AuthRoutes
from src.core.validators import ErrResp

oauth_bearer = OAuth2PasswordBearer(
    tokenUrl=AuthRoutes.POST_CREATE_USER_FORM,
)

error = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail=ErrResp(
        error_type=MessageError.INVALID_TOKEN_ERR,
        error_message=MessageError.INVALID_TOKEN_ERR_MESSAGE,
    ).model_dump(),
    headers=Headers.WWW_AUTH_BEARER,
)


async def token_is_alive(
    token: Annotated[str, Depends(oauth_bearer)],
) -> dict:
    """Validate token.

    Args:
        - token (str): HTTPBearer API key for authentication.
    Raises:
        HTTPException:
            - status 401
            - headers={"WWW-Authenticate": "Bearer"}
    """
    try:
        return decode_jwt(jwt_token=token)
    except InvalidTokenError:
        raise error


async def token_access(
    token: Annotated[dict, Depends(token_is_alive)],
):
    """Check HTTP header: Authenticate: Bearer.

    Args:
        - token (str): HTTPBearer API key for authentication.

    Raises:
        HTTPException:
            - status 401
            - headers={"WWW-Authenticate": "Bearer"}
    """
    try:

        if token.get(JWT.TOKEN_TYPE_FIELD) == JWT.TOKEN_TYPE_ACCESS:
            return token.get(JWT.PAYLOAD_SUB_KEY)
        raise InvalidTokenError

    except InvalidTokenError:
        raise error
