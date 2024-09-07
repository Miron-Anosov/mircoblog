"""Tweets for micro_blog."""

from typing import Annotated

from fastapi import APIRouter, Depends, status

from ..settings.routes_path import PathRoutes
from ..validators.valid_tweet import (
    ValidGETModelTweet,
    ValidPostModelNewTweetInput,
    ValidPostModelNewTweetOutput,
    ValidStatusModelTweetOrUser,
)
from .controller_dependends.http_handler_api_key import api_key_depend

tweets = APIRouter(tags=["Tweets"], prefix=PathRoutes.PREFIX.value)


@tweets.post(
    path=PathRoutes.TWEETS.value,
    status_code=status.HTTP_201_CREATED,
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
    response_model=ValidStatusModelTweetOrUser,
)
def delete_post_by_id(
    tweet_id: str,
    api_key: Annotated[str, Depends(api_key_depend)],
) -> ValidStatusModelTweetOrUser:
    """
    Delete a tweet by ID.

     **Headers**:
    - `api_key (str)*`: API key for authentication.

    **Path Parameters**:
    - `tweet_id (int)`: The ID of the tweet to delete.
    """
    return ValidStatusModelTweetOrUser()  # TODO: заглушка, прикрутить CRUD


@tweets.post(
    path=PathRoutes.TWEETS_POST_DEL_ID_LIKE.value,
    status_code=status.HTTP_201_CREATED,
    response_model=ValidStatusModelTweetOrUser,
)
def tweet_like_by_id(
    tweet_id: str,
    api_key: Annotated[str, Depends(api_key_depend)],
) -> ValidStatusModelTweetOrUser:
    """
    Like a tweet by ID.

     **Headers**:
    - `api_key (str)*`: API key for authentication.

    **Path Parameters**:
    - `tweet_id (int)`: The ID of the tweet to like.
    """
    return ValidStatusModelTweetOrUser()  # TODO: заглушка, прикрутить CRUD


@tweets.delete(
    path=PathRoutes.TWEETS_POST_DEL_ID_LIKE.value,
    response_model=ValidStatusModelTweetOrUser,
)
def delete_like_by_id(
    tweet_id: str,
    api_key: Annotated[str, Depends(api_key_depend)],
) -> ValidStatusModelTweetOrUser:
    """
    Delete a like of tweet by ID.

     **Headers**:
    - `api_key (str)*`: API key for authentication.

    **Path Parameters**:
    - `tweet_id (int)`: The ID of the like of tweet to delete.
    """
    # Заглушка для возвращаемого значения
    return ValidStatusModelTweetOrUser()  # TODO: заглушка, прикрутить CRUD


@tweets.get(path=PathRoutes.TWEETS.value)
def get_tweets(
    api_key: Annotated[str, Depends(api_key_depend)],
) -> ValidGETModelTweet:
    """
    Get tweets.

     **Headers**:
    - `api_key (str)*`: API key for authentication.
    """
    return ValidGETModelTweet()  # TODO: заглушка, прикрутить CRUD
