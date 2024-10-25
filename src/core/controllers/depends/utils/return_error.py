"""Common Raise HTTPException."""

import uuid
from typing import Optional

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


def raise_http_500_if_none(is_none_result: Optional[bool]) -> None:
    """Checker None.

    Args:
        - is_none_result (Optional[bool]): result db.
    Raise:
        - HTTPException
    Nones:
        - If db finish incorrect a process than it'll return None.
    """
    if is_none_result is None:
        # todo: add logger info fail get tweets data from db
        raise http_exception(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error_type=MessageError.TYPE_ERROR_INTERNAL_SERVER_ERROR,
            error_message=MessageError.MESSAGE_SERVER_ERROR,
        )


def valid_id_or_error_422(request_id: str):
    """Validate the given UUID.

    Args:
        request_id (str): The identifier as a string.

    Raises:
        HTTPException: If `request_id` is invalid,
        raises HTTP 422 with an error message.
    """
    try:
        uuid.UUID(request_id)
    except ValueError:
        raise http_exception(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            error_type=MessageError.INVALID_ID_ERR,
            error_message=MessageError.INVALID_ID_ERR_MESSAGE,
        )


def raise_http_404(
    error_type: str = MessageError.INVALID_ID_ERR,
    error_message: str = MessageError.INVALID_ID_ERR_MESSAGE_404,
    status_code: int = status.HTTP_404_NOT_FOUND,
):
    """Raise an HTTP 404 exception with a specified error message and type.

    Args:
        error_type (str): The type of the error to raise. Defaults to
            `MessageError.INVALID_ID_ERR`.
        error_message (str): The error message to display. Defaults to
            `MessageError.INVALID_ID_ERR_MESSAGE_404`.
        status_code (int): The HTTP status code to return. Defaults to
            `status.HTTP_404_NOT_FOUND`.

    Raises:
        HTTPException: Raises an HTTP 404 exception with the specified
            details.
    """
    raise http_exception(
        status_code=status_code,
        error_type=error_type,
        error_message=error_message,
    )
