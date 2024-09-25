"""Error Response to clients."""

import pydantic


class ValidErrResponse(pydantic.BaseModel):
    """Response error.

    If Api will have any errors, it will send to client.
    """

    result: bool
    error_type: str
    error_message: str

    model_config = pydantic.ConfigDict(title="Bad Request")
