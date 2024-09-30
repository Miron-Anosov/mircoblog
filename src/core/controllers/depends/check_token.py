"""Depends-Check active user."""

from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
from jwt.exceptions import ExpiredSignatureError

from src.core.controllers.depends.jwt_token import decode_jwt
from src.core.validators import ErrResp

http_bearer = HTTPBearer()


async def token_is_alive(
    token: Annotated[HTTPAuthorizationCredentials, Depends(http_bearer)],
):
    """Check HTTP header: api_key.

    Args:
        - token (str): HTTPBearer API key for authentication.
        - session (AsyncSession): get db session.
        - crud (Crud): crud worker.
    Raises:
        HTTPException:
            - status 401
            - headers={"WWW-Authenticate": "Bearer"}
    """
    try:
        return decode_jwt(jwt_token=token.credentials).get("sub")
    except ExpiredSignatureError as e:
        message_index = 0
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=ErrResp(
                error_type=str(e.args[message_index]),
                error_message="Please repeat authentication.",
            ).model_dump(),
            headers={"WWW-Authenticate": "Bearer"},
        )
