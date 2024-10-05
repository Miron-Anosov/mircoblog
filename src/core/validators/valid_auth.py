"""Validate new user.."""

import pydantic


class ValidateNewUser(pydantic.BaseModel):
    """**Model for tweet author details**.

    - `name`: User's name.
    - `password`: secret.
    - `user_email`: user email.
    """

    name: str = pydantic.Field(
        description="Author's name: English, digits and one underscore.",
        min_length=2,
        max_length=15,
        pattern=r"^[a-zA-Z0-9_]+$",
    )

    password: bytes = pydantic.Field(
        min_length=8, max_length=64, description="User's secret."
    )
    password_control: bytes = pydantic.Field(
        min_length=8,
        max_length=64,
        description="User's secret for check both.",
        alias="repeat password",
    )
    user_email: pydantic.EmailStr = pydantic.Field(
        alias="email", description="User's email."
    )
    model_config = pydantic.ConfigDict(title="NewUser")


class ValidateLoginUser(pydantic.BaseModel):
    """**Model for tweet author details**.

    - `email`: User's email.
    - `password`: secret.
    """

    user_email: pydantic.EmailStr = pydantic.Field(
        alias="email", description="User's email."
    )
    password: bytes = pydantic.Field(
        min_length=1, max_length=64, description="User's secret."
    )
    model_config = pydantic.ConfigDict(title="LoginUser")
