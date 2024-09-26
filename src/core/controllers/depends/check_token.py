"""There are controllers API of depends."""

from typing import Annotated

from fastapi import Depends, Header, HTTPException, status
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.controllers.depends.connect_db import get_session
from src.core.validators import UserToken


async def token_depends(
    api_key: Annotated[
        str | None,
        Header(
            alias="x-auth-token", alias_priority=1, description="x-auth-token"
        ),
    ],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """Check HTTP header: api_key.

    Args:
    - api_key (str): API key for authentication. Min length 6. Max length 60.
    """
    try:
        UserToken(api_key=api_key)
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="api-key is invalid.",
        )
    else:
        return api_key
