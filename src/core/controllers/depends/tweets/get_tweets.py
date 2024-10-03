"""Return tweets."""

from typing import TYPE_CHECKING, Annotated

from fastapi import Depends, status

from src.core.controllers.depends.utils.connect_db import get_crud, get_session
from src.core.controllers.depends.utils.return_error import http_exception
from src.core.settings.const import MessageError
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

    if tweets is None:
        # todo: add logger info fail get tweets data from db
        raise http_exception(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error_type=MessageError.TYPE_ERROR_INTERNAL_SERVER_ERROR,
            error_message=MessageError.MESSAGE_SERVER_ERROR,
        )

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
                        user_id=user_like.id,
                        name=user_like.name,
                    )
                    for user_like in tweet.likes
                ],
            )
            for tweet in tweets
        ]
    )
