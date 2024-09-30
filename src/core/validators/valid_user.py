"""Validator models for /tweets.

You can see route to /src/back_core/controllers/users.py
"""

import pydantic


class ValidUserModel(pydantic.BaseModel):
    """**Model for tweet author details**.

     - `id`: str: Identification of user.
    - `name`: User's name.
    """

    id: str = pydantic.Field(
        description="Author's unique ID",
    )
    name: str = pydantic.Field(
        ..., description="Author's name", min_length=2, max_length=15
    )

    model_config = pydantic.ConfigDict(title="User")


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
        title="User's profile",
        from_attributes=True,
        extra="ignore",
        json_schema_extra={
            "example": {
                "result": True,
                "user": {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "name": "Dick",
                    "followers": [
                        {
                            "id": "3fa33364-5717-4562-b3fc-2c963f66afa6",
                            "name": "Tom",
                        }
                    ],
                    "following": [
                        {
                            "id": "3fa33364-5717-4562-b3fc-2c963f4563fa",
                            "name": "Ramil",
                        }
                    ],
                },
            }
        },
    )
