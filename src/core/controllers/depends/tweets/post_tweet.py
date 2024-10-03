"""Post new tweet."""

from typing import TYPE_CHECKING, Annotated

from fastapi import Depends

from src.core.controllers.depends.auth.check_token import (
    get_user_id_by_token_access,
)
from src.core.controllers.depends.connect_db import get_crud, get_session
from src.core.validators import PostNewTweet, ReturnNewTweet

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from src.core.models_orm.crud import Crud


async def tweet_data(
    id_user: Annotated[str, Depends(get_user_id_by_token_access)],
    tweet: PostNewTweet,
    session: Annotated["AsyncSession", Depends(get_session)],
    crud: Annotated["Crud", Depends(get_crud)],
) -> "ReturnNewTweet":
    """Return tweets."""
    tweet_id = await crud.tweets.post_tweet(
        user_id=id_user,
        session=session,
        content_test=tweet.tweet_data,
        content_media_ids=tweet.tweet_media_ids,
    )
    return ReturnNewTweet(tweet_id=tweet_id)
