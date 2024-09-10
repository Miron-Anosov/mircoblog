"""POST /tweets/{id}/like.

Create like of tweet.
"""

from back_core.validators import StatusResponse


async def post_like_by_id(tweet_id: str) -> StatusResponse:
    """
    Like a tweet by ID.

     **Headers**:
    - `api_key (str)*`: API key for authentication.

    **Path Parameters**:
    - `tweet_id (int)`: The ID of the tweet to like.
    """
    pass  # TODO: заглушка, прикрутить CRUD
