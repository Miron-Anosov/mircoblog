"""Depends-Check active user."""

from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError

from src.core.controllers.depends.utils.jwt_token import decode_jwt
from src.core.validators import ErrResp

oauth_bearer = OAuth2PasswordBearer(
    tokenUrl="/api/auth/login/form",
    scheme_name="Authorizations",
    description="Authorizations and get token.",
)


async def token_is_alive(
    token: Annotated[str, Depends(oauth_bearer)],
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
        return decode_jwt(jwt_token=token).get("sub")
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=ErrResp(
                error_type="Invalid token.",
                error_message="Please repeat authentication.",
            ).model_dump(),
            headers={"WWW-Authenticate": "Bearer"},
        )
