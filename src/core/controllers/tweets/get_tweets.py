"""GET /tweets/."""

from typing import Annotated

from fastapi import Depends

from src.core.controllers.depends.tweets.get_tweets import get_tweets_data
from src.core.validators import GetAllTweets


async def get_tweets(
    tweets: Annotated["GetAllTweets", Depends(get_tweets_data)]
) -> "GetAllTweets":
    """
    Get tweets.

     **Headers**:
    - Authorization: Bearer `access_token` (str): User key authentication.
    """
    return tweets
