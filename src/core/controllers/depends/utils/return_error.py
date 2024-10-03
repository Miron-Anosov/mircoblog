"""Common Raise HTTPException."""

from fastapi import HTTPException, status

from src.core.settings.const import MessageError
from src.core.validators import ErrResp


def http_exception(
    status_code: int = status.HTTP_401_UNAUTHORIZED,
    error_type=MessageError.INVALID_TOKEN_ERR,
    error_message=MessageError.INVALID_TOKEN_ERR_MESSAGE,
    headers: dict[str, str] | None = None,
) -> HTTPException:
    """Return HTTPException.

    Args:
        - status_code (int): HTTP status.
        - error_type (str): Type error.
        - error_message (str): Message error.
        - headers (dict[str, str] | None): If it is requirement.
    Raise:
        - HTTPException

    """
    return HTTPException(
        status_code=status_code,
        detail=ErrResp(
            error_type=error_type,
            error_message=error_message,
        ).model_dump(),
        headers=headers,
    )
