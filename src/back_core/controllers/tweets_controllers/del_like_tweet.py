"""DELETE /tweets/{id}/like.

del like of tweet.
"""

from back_core.validators import StatusResponse


async def del_like_tweet_by_id(tweet_id: str) -> StatusResponse:
    """
    Del Like a tweet by ID.

     **Headers**:
    - `api_key (str)*`: API key for authentication.

    **Path Parameters**:
    - `tweet_id (int)`: The ID of the tweet to delete.
    """
    return StatusResponse()
