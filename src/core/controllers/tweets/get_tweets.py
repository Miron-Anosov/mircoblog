"""GET /tweets/."""

from typing import Annotated

from fastapi import Depends
from fastapi_cache.decorator import cache

from src.core.controllers.depends.tweets.get_tweets import get_tweets_data
from src.core.settings.const import CacheExpirationTime
from src.core.validators import GetAllTweets


@cache(expire=CacheExpirationTime.CACHE_EXPIRATION_TIME_GET_TWEETS)
async def get_tweets(
    tweets: Annotated["GetAllTweets", Depends(get_tweets_data)]
) -> "GetAllTweets":
    """
    Get tweets.

    Args:
        tweets (GetAllTweets): The tweets data dependency.

    Returns:
        GetAllTweets: The retrieved tweets.
    """
    return tweets
