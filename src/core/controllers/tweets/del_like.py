"""DELETE /tweets/{id}/like.

del like of tweet.
"""

from src.core.validators import StatusResponse


async def del_like(tweet_id: str) -> StatusResponse:
    """
    Del Like a tweet by ID.

     **Headers**:
    - `x-auth-token (str)*`: User key authentication.

    **Path Parameters**:
    - `tweet_id (int)`: The ID of the tweet to delete.
    """
    return StatusResponse()
