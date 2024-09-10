"""POST /tweets.

Create a new tweet.
"""

from back_core.validators import PostNewTweet, ReturnNewTweet


async def post_new_tweet(tweet: PostNewTweet) -> ReturnNewTweet:
    """
    Create a new tweet.

    **Headers**:
    - `api_key (str)*`: API key for authentication.

    **Body**:
    - `tweet_data (str)*`: The text content of the tweet.
    - `tweet_media_ids (Array[int])`: A list of media IDs (e.g., images)<br>
     associated with the tweet.

    **Notes**:
    - The `tweet_media_ids` parameter is optional.
    - Images can be uploaded using the `/api/media` endpoint.
     The frontend will automatically handle the image
     upload before submitting the tweet and will include
     the image IDs in the request.
    """
    pass  # TODO: заглушка, прикрутить CRUD
