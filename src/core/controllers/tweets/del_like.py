"""DELETE /tweets/{id}/like.

del like of tweet.
"""

from typing import Annotated

from fastapi import Depends

from src.core.controllers.depends.tweets.like import delete_like
from src.core.validators import StatusResponse


async def del_like(_: Annotated[bool, Depends(delete_like)]) -> StatusResponse:
    """
    Del Like a tweet by ID.

     **Headers**:
    - Authorization: Bearer `access_token` (str): User key authentication.

    **Path Parameters**:
    - `tweet_id (str)`: The ID of the tweet to delete a like.
    """
    return StatusResponse()
