"""Validator models for /tweets.

You can see route to /src/back_core/controllers/tweets.py
"""

import uuid

import pydantic

from .valid_likes import ValidLikeModel
from .valid_user import ValidUserModel


class ValidPostModelNewTweetInput(pydantic.BaseModel):
    """**Model validate input date from route POST /tweets**.

    - `tweet_data`: str: Data post tweet.
    - `tweet_media_ids`: Pictures id with tweet.
    """

    tweet_data: str = pydantic.Field(description="Message to new post")
    tweet_media_ids: list[int] | None = pydantic.Field(
        strict=False, description="Array tweet IDs"
    )
    model_config = pydantic.ConfigDict(title="Tweet Request")


class ValidPostModelNewTweetOutput(pydantic.BaseModel):
    """**Movel validate response POST /tweets**.

    - `result`: bool : Successful or unsuccessful.
    - `tweet_id`: UUID : Unique identifier for the tweet.
    """

    result: bool = pydantic.Field(
        description="Successful or unsuccessful",
    )
    tweet_id: uuid.UUID = pydantic.Field(
        default_factory=uuid.uuid4,
        description="Unique identifier for " "the tweet.",
    )

    model_config = pydantic.ConfigDict(title="Tweet Response")


class ValidStatusResponse(pydantic.BaseModel):
    """**Movel validate response status  /tweets /users**.

    - `result`: bool : Successful or unsuccessful.

    """

    result: bool = True
    model_config = pydantic.ConfigDict(title="Status OK")


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

    result: bool
    content: str = pydantic.Field(..., description="Content of the tweet")
    attachments: list[pydantic.HttpUrl] | None = pydantic.Field(
        None, description="List of attachment links for the tweet"
    )
    author: ValidUserModel = pydantic.Field(
        ..., description="Author of the tweet"
    )
    likes: list[ValidLikeModel] | None = pydantic.Field(
        [], description="List of users who liked the tweet"
    )

    model_config = pydantic.ConfigDict(
        from_attributes=True,
        title="Get Tweets Response",
        json_schema_extra={
            "example": {
                "result": True,
                "tweets": [
                    {
                        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",  # noqa E501
                        "content": "This is a sample tweet",
                        "attachments": [
                            "/media/images/12345.jpg",
                            "/media/images/12346.jpg",
                        ],
                        "author": {
                            "id": "3fa85f64-4578-4562-b3fh-2c963867ytg4",  # noqa E501
                            "name": "Author Name",
                        },
                        "likes": [
                            {
                                "user_id": "3fa85f64-5555-4562-b3fc-2c963g66afb3",  # noqa E501
                                "name": "User1",
                            },
                        ],
                    },
                ],
            }
        },
    )
