"""Return tweets."""

from typing import TYPE_CHECKING, Annotated

from fastapi import Depends, Header, Request, Response
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from src.core.controllers.depends.utils.connect_db import get_crud, get_session
from src.core.controllers.depends.utils.redis_chash import cache_get_response
from src.core.controllers.depends.utils.return_error import (
    http_exception,
    raise_http_db_fail,
)
from src.core.settings.const import CacheConf, MessageError
from src.core.validators import GetAllTweets, Like, User

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from src.core.models_orm.crud import Crud


@cache_get_response(
    expire=CacheConf.CACHE_EXPIRATION_TIME_GET_TWEETS,
    prefix_key=CacheConf.PREFIX_GET_TWEETS,
)
async def get_tweets_data(
    session: Annotated["AsyncSession", Depends(get_session)],
    crud: Annotated["Crud", Depends(get_crud)],
    request: Request,
    response: Response,
    if_none_match: str | None = Header(default=None),
) -> "GetAllTweets":
    """
    Retrieve and return all tweets.

    This function fetches tweets from the database, validates the response,
    and returns a list of tweets along with their authors and likes.

    Args:
        session (AsyncSession): Database session used for querying.
        crud (Crud): CRUD instance for handling tweet operations.
        request (Request): HTTP request object for cache handling.
        response (Response): HTTP response object to set cache headers.
        if_none_match (str | None): Optional ETag header for cache validation.

    Returns:
        GetAllTweets: Pydantic model representing the list of tweets with authors
        and likes.

    Raises:
        HTTPException: If no tweets are found or there's an internal server error.

    Notes:
        The function uses caching to reduce load on the database and improve
        performance. The sleep of 3 seconds is used for testing purposes.
    """  # noqa E501

    tweets = await crud.tweets.get_tweets(session=session)
    raise_http_db_fail(is_none_result=tweets)

    if not tweets:
        # TODO LOGGER INFO {id} {request} {response} {if_none_match}
        print(request, response, if_none_match)
        http_exception(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            error_message=MessageError.MESSAGE_USER_NOT_FOUND,
            error_type=MessageError.TYPE_ERROR_500,
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
