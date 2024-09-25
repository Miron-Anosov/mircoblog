"""POST /tweets/{id}/like.

Create like of tweet.
"""

from src.core.validators import StatusResponse


async def post_like_by_id(tweet_id: str) -> "StatusResponse":
    """
    Like a tweet by ID.

     **Headers**:
    - `x-auth-token (str)*`: User key authentication.

    **Path Parameters**:
    - `tweet_id (int)`: The ID of the tweet to like.
    """
    return StatusResponse()
