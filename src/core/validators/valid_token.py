"""Valid User token."""

import pydantic


class ValidTokenInfo(pydantic.BaseModel):
    """User's uniq api-key.

    `access_token` uses for authorisation for users.
    `token_type`: Bearer
    """

    access_token: str = pydantic.Field(
        description="String key.",
        min_length=6,
        max_length=60,
    )
    token_type: str = "Bearer"
    model_config = pydantic.ConfigDict(title="Token")
