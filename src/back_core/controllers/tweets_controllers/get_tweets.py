"""GET /tweets/."""

from back_core.validators import GetAllTweets


async def get_tweets() -> GetAllTweets:
    """
    Get tweets.

     **Headers**:
    - `api_key (str)*`: API key for authentication.
    """
    pass  # TODO: заглушка, прикрутить CRUD
