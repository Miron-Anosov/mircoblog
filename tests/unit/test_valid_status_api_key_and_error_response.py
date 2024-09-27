"""Test status model, api-key model and error response model."""

import pytest
from pydantic import ValidationError

from src.core.validators import ErrResp, UserToken
from src.core.validators.valid_status_ok import ValidStatusResponse


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

    assert ErrResp(**data_response_valid)

    with pytest.raises(ValidationError):
        assert ErrResp(**data_response_invalid)


def test_valid_api_key_model() -> None:
    """Test model ValidApiKey."""
    invalid_key = {"api_key": "key"}
    with pytest.raises(ValidationError):
        UserToken(**invalid_key)

    too_long_key = {"api_key": "key" * 21}
    with pytest.raises(ValidationError):
        UserToken(**too_long_key)

    int_key = {"api_key": 123234}
    with pytest.raises(ValidationError):
        UserToken(**int_key)

    empty_key = {"api_key": ""}
    with pytest.raises(ValidationError):
        UserToken(**empty_key)

    valid_key = {"access_token": "api-key", "token_type": ""}
    assert UserToken(**valid_key)

    valid_vol_int = {"access_token": "api-key", "token_type": "12123"}
    assert UserToken(**valid_vol_int)
