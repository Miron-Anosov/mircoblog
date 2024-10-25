"""POST /tweets/{id}/like.

Create like of tweet.
"""

from typing import Annotated

from fastapi import Depends

from src.core.controllers.depends.tweets.like import post_like
from src.core.validators import StatusResponse


async def post_like_by_id(
    like: Annotated[bool, Depends(post_like)]
) -> "StatusResponse":
    """
    Like a tweet by ID.

     **Headers**:
    - Authorization: Bearer `access_token` (str): User key authentication.

    **Path Parameters**:
    - `tweet_id (str)`: The ID of the tweet to like.
    """
    return StatusResponse(result=like)
