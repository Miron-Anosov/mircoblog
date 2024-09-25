"""Valid user session."""

import secrets
from typing import Annotated

from fastapi import Depends, Header
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.controllers.controller_depends.connect_db import get_session


async def authorization_user_id_by_api_key(
    api_key: Annotated[
        str | None,
        Header(
            alias="x-auth-token", alias_priority=1, description="x-auth-token"
        ),
    ],
    session: Annotated[AsyncSession, Depends(get_session)],
) -> str | None:
    """Check authorization user."""
    user_in_db = await session.get(api_key, "s")
    return user_in_db if user_in_db else None
    # TODO: REBUILD. IT's FAKE logic!


#
# async def authorization_user_by_login(
#
# )
