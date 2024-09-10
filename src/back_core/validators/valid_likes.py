"""Validator like models for /tweets.

You can see route to /src/back_core/controllers/
"""

import pydantic


class ValidLikeModel(pydantic.BaseModel):
    """**Likes of tweet**."""

    user_id: int = pydantic.Field(
        ..., description="User's unique ID who liked the tweet"
    )
    name: str = pydantic.Field(..., description="User's name")
    model_config = pydantic.ConfigDict(title="Like Tweet")
