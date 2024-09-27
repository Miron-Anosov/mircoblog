"""Valid user session."""

from typing import Annotated

from fastapi import Depends, Header
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.controllers.depends.connect_db import get_session


async def get_id_by_token(
    api_key: Annotated[
        str | None,
        Header(
            alias="x-auth-token",
            alias_priority=1,
            description="x-auth-token",
        ),
    ],
    session: Annotated[AsyncSession, Depends(get_session)],
) -> str | None:
    """Check authorization user."""
    user_in_db = await session.get(api_key, "s")
    return user_in_db if user_in_db else None
    # TODO: REBUILD. IT's FAKE logic!
