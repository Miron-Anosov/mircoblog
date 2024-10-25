"""GET /tweets/."""

from typing import Annotated

from fastapi import Depends

from src.core.controllers.depends.tweets.get_tweets import get_tweets_data
from src.core.validators import GetAllTweets


async def get_tweets(
    tweets: Annotated["GetAllTweets", Depends(get_tweets_data)]
) -> GetAllTweets:
    """
        Get a list of tweets.

        **Headers**:
        - Authorization: Bearer `access_token` (str): User key authentication.
        - If-None-Match: (str) ETag value for cache validation.

        **Query Parameters**:
        - No query parameters are required for this endpoint.

        **Response**:
        - A JSON object containing the list of tweets and their details.

        **Response Fields**:
        - `result (bool)`: Indicates if the request was successful.
        - `tweets (List)`: A list of tweet objects, where each tweet contains:
            - `id (str)`: Unique identifier of the tweet.
            - `content (str)`: The text content of the tweet.
            - `attachments (List[str], optional)`: URLs of attached media.
            - `author (dict)`: Tweet author's information:
                - `id (str)`: Unique identifier of the author.
                - `name (str)`: Name of the author.
            - `likes (List[dict])`: Users who liked the tweet, each containing:
                - `user_id (str)`: Unique identifier of the user.
                - `name (str)`: Name of the user.

    **Notes**:
    - The `likes` field contains user data for those who liked the tweet.
    - Attachments are optional and may include media files uploaded by the user.
    """  # noqa E501

    # TODO: Add log INFO: GET BEFORE CHASH DATA
    return tweets
