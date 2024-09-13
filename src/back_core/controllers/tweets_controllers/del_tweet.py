"""DELETE /tweets/{id}.

Delete tweet.
"""

from src.back_core.validators import StatusResponse


async def del_tweet_by_id(tweet_id: str) -> StatusResponse:
    """
    Delete a tweet by ID.

     **Headers**:
    - `api_key (str)*`: API key for authentication.

    **Path Parameters**:
    - `tweet_id (int)`: The ID of the tweet to delete.
    """
    pass  # TODO: заглушка, прикрутить CRUD
