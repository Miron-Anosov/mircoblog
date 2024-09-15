"""Test status model, api-key model and error response model."""

import pytest
from pydantic import ValidationError

from src.back_core.validators.valid_common_status_ok import ValidStatusResponse
from src.back_core.validators.valid_error_response_and_apy_key import (
    ValidApiKey,
    ValidErrorResponse,
)


def test_valid_status_ok_model() -> None:
    """Test movel ValidStatusResponse."""
    assert ValidStatusResponse(**{"result": True})
    assert ValidStatusResponse(**{"result": False})
    assert ValidStatusResponse(**{"result": 1})
    assert ValidStatusResponse(**{"result": 0})
    assert ValidStatusResponse(**{"result": "true"})
    assert ValidStatusResponse(**{"result": "false"})
    assert ValidStatusResponse(**{"result": "yes"})
    assert ValidStatusResponse(**{"result": "YES"})
    assert ValidStatusResponse(**{"result": "no"})
    assert ValidStatusResponse(**{"result": "NO"})

    with pytest.raises(ValidationError):
        ValidStatusResponse(**{"result": bool})

    with pytest.raises(ValidationError):
        assert ValidStatusResponse(**{"result": ""})

    with pytest.raises(ValidationError):
        assert ValidStatusResponse(**{"result": "agree"})


def test_error_response() -> None:
    """Test model ValidErrorResponse."""
    data_response_valid: dict = {
        "result": True,
        "error_type": "Exception",
        "error_message": "Allert",
    }

    data_response_invalid: dict = {
        "result": True,
        "error_type": Exception,
        "error_message": "Allert",
    }

    assert ValidErrorResponse(**data_response_valid)

    with pytest.raises(ValidationError):
        assert ValidErrorResponse(**data_response_invalid)


def test_valid_api_key_model() -> None:
    """Test model ValidApiKey."""
    too_short_key = {"api_key": "key"}
    with pytest.raises(ValidationError):
        assert ValidApiKey(**too_short_key)

    too_long_key = {"api_key": "key" * 21}
    with pytest.raises(ValidationError):
        assert ValidApiKey(**too_long_key)

    int_key = {"api_key": 123234}
    with pytest.raises(ValidationError):
        assert ValidApiKey(**int_key)

    empty_key = {"api_key": ""}
    with pytest.raises(ValidationError):
        assert ValidApiKey(**empty_key)

    valid_key = {"api_key": "api-key"}
    assert ValidApiKey(**valid_key)

    valid_key_int = {"api_key": "api-key-1234"}
    assert ValidApiKey(**valid_key_int)
