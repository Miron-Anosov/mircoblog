"""Validator models for GET /tweets.

You can see route to /src/back_core/controllers/tweets.py
"""

import uuid

import pydantic

from src.core.settings.const import PydanticTweets

from .valid_likes import ValidLikeModel
from .valid_user import ValidUserModel


class ValidateGetTweet(pydantic.BaseModel):
    """**Data response tweets**.

    - `id` : Unique identifier for the tweet
    - `content` : User's data of tweet
    - `tweets` : list[ValidDataGetTweetOutput]
    - `author` : ValidUserModel
    - `likes` : list[ValidLikeModel]
    """

    id: uuid.UUID = pydantic.Field(
        default_factory=uuid.uuid4,
        description=PydanticTweets.ID_DESCRIPTION,
    )
    content: str
    attachments: list[str] = pydantic.Field(
        default=[], description=PydanticTweets.ATTACHMENTS_DESCRIPTION
    )
    author: ValidUserModel
    likes: list[ValidLikeModel]

    model_config = pydantic.ConfigDict(
        from_attributes=True,
        title=PydanticTweets.TITLE_TWEET,
    )


class ValidGETModelTweet(pydantic.BaseModel):
    """**Model to validate GET /tweets**.

    - `result`: bool : Successful or unsuccessful.
    - `tweets`: List of tweet objects containing the following fields:
        - `id`: int : Unique identifier of the tweet.
        - `content`: string : Content of the tweet.
        - `attachments`: List of URLs (optional)
        pointing to media files attached to the tweet.
        - `author`: Author object with the following fields:
            - `id`: int : Unique identifier of the author.
            - `name`: string : Name of the author.
        - `likes`: List of users who liked the tweet, each containing:
            - `user_id`: int : Unique identifier of the user.
            - `name`: string : Name of the user.
    """

    result: bool = True
    tweets: list[ValidateGetTweet]

    model_config = pydantic.ConfigDict(
        from_attributes=True,
        title=PydanticTweets.TITLE_GET_TWEETS_RESPONSE,
        json_schema_extra=PydanticTweets.JSON_SCHEMA_TWEET,
    )
