"""Tweets for micro_blog."""

from typing import Annotated

from fastapi import APIRouter, Depends

from ..settings.routes_path import PathRoutes
from ..validators.validation_tweet import (
    ValidPostModelNewTweetInput,
    ValidPostModelNewTweetOutput,
    ValidStatusModelTweet,
)
from .controller_dependends.http_handler_api_key import api_key_depend

tweets = APIRouter(tags=["Tweets"], prefix=PathRoutes.PREFIX.value)


@tweets.post(
    path=PathRoutes.TWEETS.value,
    status_code=201,
    response_model=ValidPostModelNewTweetOutput,
)
def post_new_tweet(
    tweet: ValidPostModelNewTweetInput,
    api_key: Annotated[str, Depends(api_key_depend)],
) -> ValidPostModelNewTweetOutput:
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
    return ValidPostModelNewTweetOutput()


@tweets.delete(
    path=PathRoutes.TWEETS_DEL_BY_ID.value,
    response_model=ValidStatusModelTweet,
)
def delete_post_by_id(
    tweet_id: int,
    api_key: Annotated[str, Depends(api_key_depend)],
) -> ValidStatusModelTweet:
    """
    Delete a tweet by ID.

     **Headers**:
    - `api_key (str)*`: API key for authentication.

    **Path Parameters**:
    - `tweet_id (int)`: The ID of the tweet to delete.
    """
    # Заглушка для возвращаемого значения
    return ValidStatusModelTweet()


@tweets.post(
    path=PathRoutes.TWEETS_ID_LIKE.value,
    status_code=201,
    response_model=ValidStatusModelTweet,
)
def tweet_like_by_id(
    tweet_id: int,
    api_key: Annotated[str, Depends(api_key_depend)],
) -> ValidStatusModelTweet:
    """
    Like a tweet by ID.

     **Headers**:
    - `api_key (str)*`: API key for authentication.

    **Path Parameters**:
    - `tweet_id (int)`: The ID of the tweet to like.
    """


@tweets.delete(
    path=PathRoutes.TWEETS_DEL_LIKE_BY_ID.value,
    response_model=ValidStatusModelTweet,
)
def delete_like_by_id(
    tweet_id: int,
    api_key: Annotated[str, Depends(api_key_depend)],
) -> ValidStatusModelTweet:
    """
    Delete a like of tweet by ID.

     **Headers**:
    - `api_key (str)*`: API key for authentication.

    **Path Parameters**:
    - `tweet_id (int)`: The ID of the like of tweet to delete.
    """
    # Заглушка для возвращаемого значения
    return ValidStatusModelTweet()
