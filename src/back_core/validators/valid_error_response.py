"""Error Response to clients."""

import pydantic


class ValidErrorResponse(pydantic.BaseModel):
    """Response error model.

    If Api will have any errors, it will send to client.
    """

    result: bool
    error_type: str
    error_message: str
