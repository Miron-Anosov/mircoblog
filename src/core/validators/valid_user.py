"""Validator models for /tweets.

You can see route to /src/back_core/controllers/users.py
"""

import pydantic

from src.core.settings.const import PydanticUser


class ValidUserModel(pydantic.BaseModel):
    """**Model for tweet author details**.

     - `id`: str: Identification of user.
    - `name`: User's name.
    """

    id: str = pydantic.Field(
        description=PydanticUser.DESCRIPTION_ID,
    )
    name: str = pydantic.Field(
        ...,
        description=PydanticUser.DESCRIPTION_NAME,
        min_length=2,
        max_length=15,
    )

    model_config = pydantic.ConfigDict(title=PydanticUser.TITLE_SWAGGER)


class ValidModelGetMe(pydantic.BaseModel):
    """Validate model for profile of user."""

    id: str
    name: str
    followers: list[ValidUserModel | None]
    following: list[ValidUserModel | None]


class ValidateUserProfile(pydantic.BaseModel):
    """**Users' profile**.

    - `result`: bool : Successful or unsuccessful.
    - `user`: Dict of user objects containing the following fields:
        - `id`: str : Unique identifier of the user.
        - `name`: string : User's name.
        - `followers`: Dict of users.
            - `id`: str : Unique identifier of the user.
            - `name`: string : User's name.
        - `following`: Dict of users.
            - `id`: str : Unique identifier of the user.
            - `name`: string : User's name.
    """

    result: bool
    user: ValidModelGetMe
    model_config = pydantic.ConfigDict(
        title=PydanticUser.TITLE,
        from_attributes=True,
        extra="ignore",
        json_schema_extra=PydanticUser.JSON_SCHEMA_USER,
    )
