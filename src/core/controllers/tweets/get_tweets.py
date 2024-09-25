"""GET /tweets/."""

from src.core.validators import GetAllTweets


async def get_tweets() -> "GetAllTweets":
    """
    Get tweets.

     **Headers**:
    - `x-auth-token (str)*`: User key authentication.
    """
    return GetAllTweets()
