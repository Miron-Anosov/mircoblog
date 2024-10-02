"""Validator models for GET /tweets.

You can see route to /src/back_core/controllers/tweets.py
"""

import uuid

import pydantic

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
        description="Unique identifier for the tweet.",
    )
    content: str
    attachments: list[str] | None = pydantic.Field(
        default=None, description="List of URLs (optional)"
    )
    author: ValidUserModel
    likes: list[ValidLikeModel]

    model_config = pydantic.ConfigDict(
        from_attributes=True,
        title="Tweet",
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
        title="Get Tweets Response",
        json_schema_extra={
            "example": {
                "result": True,
                "tweets": [
                    {
                        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                        "content": "This is a sample tweet",
                        "attachments": [
                            "/media/images/12345.jpg",
                            "/media/images/12346.jpg",
                        ],
                        "author": {
                            "id": "3fa85f64-4578-4562-b3fc-2c963f66afa6",
                            "name": "Author Name",
                        },
                        "likes": [
                            {
                                "user_id": "3fa85f64-5555-4562-b3fc-2c963f66afa6",  # noqa E501
                                "name": "User1",
                            },
                        ],
                    },
                ],
            }
        },
    )
