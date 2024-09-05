"""There are controllers API of depends."""

from typing import Annotated

from fastapi import Header, HTTPException


def api_key_depend(api_key: Annotated[str | None, Header()]):
    """Check HTTP header: api_key.

    api_key: str| None: user's api_key.
    """
    if api_key is None:
        raise HTTPException(status_code=400, detail="API key is required")

    pass
