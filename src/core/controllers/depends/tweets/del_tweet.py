"""Dependency del tweet.

/api/tweets/{id}
"""

from typing import TYPE_CHECKING, Annotated

from fastapi import Depends, status

from src.core.controllers.depends.auth.check_token import (
    get_user_id_by_token_access,
)
from src.core.controllers.depends.utils.connect_db import get_crud, get_session
from src.core.controllers.depends.utils.return_error import http_exception
from src.core.settings.const import MessageError

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from src.core.models_orm.crud import Crud


async def del_tweet(
    tweet_id: str,
    id_user: Annotated[str, Depends(get_user_id_by_token_access)],
    session: Annotated["AsyncSession", Depends(get_session)],
    crud: Annotated["Crud", Depends(get_crud)],
) -> bool:
    """Delete tweet and likes from db."""
    result = await crud.tweets.delete_tweet(
        session=session, id_tweet=tweet_id, id_user=id_user
    )
    if result is None:
        raise http_exception(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error_type=MessageError.TYPE_ERROR_INTERNAL_SERVER_ERROR,
            error_message=MessageError.MESSAGE_SERVER_ERROR,
        )
    return True
