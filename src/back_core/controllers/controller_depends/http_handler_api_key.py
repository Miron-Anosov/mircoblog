"""There are controllers API of depends."""

from typing import Annotated

from fastapi import Header, HTTPException, status
from pydantic import ValidationError

from src.back_core.validators.valid_error_response_and_apy_key import (
    ValidApiKey,
)


def api_key_depend(api_key: Annotated[str | None, Header()]):
    """Check HTTP header: api_key.

    Args:
     - api_key (str): API key for authentication. Min length 6. Max length 60.
    """
    try:
        ValidApiKey(api_key=api_key),
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="api-key is invalid.",
        )

    pass  # todo: use api-key
