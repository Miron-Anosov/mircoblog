"""Test valid models."""

import pytest
from pydantic import ValidationError

from src.back_core.validators.valid_user import ValidateUserProfile
from tests.common_data import user_data


def test_user_profile_model() -> None:
    """Test user model."""
    assert ValidateUserProfile(**user_data)
    user = ValidateUserProfile(**user_data)
    assert user.result is True
    assert user.user.name == "Dick"
    assert len(user.user.followers) == 1
    assert len(user.user.following) == 1

    invalid_data = {
        "result": "Not a boolean",
        "user": {
            "name": "Dick",
            # Empty id
            "followers": [],
            "following": [],
        },
    }

    with pytest.raises(ValidationError):
        ValidateUserProfile(**invalid_data)
