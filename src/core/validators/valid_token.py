"""Valid User token."""

import pydantic


class ValidTokenInfo(pydantic.BaseModel):
    """User's uniq api-key.

    `access_token` uses for authorisation for users.
    `token_type`: Bearer
    """

    access_token: str = pydantic.Field(
        description="JWT token.",
    )
    token_type: str = "Bearer"
    model_config = pydantic.ConfigDict(title="Token")
