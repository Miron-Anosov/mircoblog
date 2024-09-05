"""Validator models for /tweets.

You can see route to /src/back_core/controllers/tweets.py
"""

import pydantic


class ValidPostModelNewTweetInput(pydantic.BaseModel):
    """Model validate input date from route /tweets.

    tweet_data: str: Data post tweet.
    tweet_media_ids: Pictures id with tweet.
    """

    tweet_data: str = pydantic.Field(description="Message to new post")
    tweet_media_ids: list[int] | None = pydantic.Field(
        strict=False, description="Array tweet ids"
    )
