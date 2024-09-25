"""DELETE /tweets/{id}.

Delete tweet.
"""

from src.core.validators import StatusResponse


async def del_tweet_by_id(tweet_id: str) -> "StatusResponse":
    """
    Delete a tweet by ID.

     **Headers**:
    - `x-auth-token (str)*`: User key authentication.

    **Path Parameters**:
    - `tweet_id (int)`: The ID of the tweet to delete.
    """
    return StatusResponse()
