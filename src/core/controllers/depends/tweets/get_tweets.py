"""Return tweets."""

from typing import TYPE_CHECKING, Annotated

from fastapi import Depends

from src.core.controllers.depends.utils.connect_db import get_crud, get_session
from src.core.controllers.depends.utils.return_error import raise_http_db_fail
from src.core.validators import GetAllTweets, Like, User

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from src.core.models_orm.crud import Crud


async def get_tweets_data(
    session: Annotated["AsyncSession", Depends(get_session)],
    crud: Annotated["Crud", Depends(get_crud)],
) -> "GetAllTweets":
    """Return tweets."""
    tweets = await crud.tweets.get_tweets(session=session)

    raise_http_db_fail(is_none_result=tweets)

    return GetAllTweets(
        tweets=[
            dict(
                id=str(tweet.id),
                content=tweet.content,
                attachments=tweet.attachments,
                author=User(
                    id=str(tweet.owner.id),
                    name=tweet.owner.name,
                ),
                likes=[
                    Like(
                        user_id=like.user.id,
                        name=like.user.name,
                    )
                    for like in tweet.likes
                    if like
                ],
            )
            for tweet in tweets
            if tweet
        ]
    )
