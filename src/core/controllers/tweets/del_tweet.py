"""DELETE /tweets/{id}.

Delete tweet.
"""

from typing import Annotated

from fastapi import Depends

from src.core.controllers.depends.tweets.del_tweet import del_tweet
from src.core.validators import StatusResponse


async def del_tweet_by_id(
    result: Annotated[bool, Depends(del_tweet)]
) -> "StatusResponse":
    """
    Delete a tweet by ID.

     **Headers**:
    - Authorization: Bearer `access_token` (str): User key authentication.

    **Path Parameters**:
    - `tweet_id (str)`: The ID of the tweet to delete.
    """
    return StatusResponse(result=result)
