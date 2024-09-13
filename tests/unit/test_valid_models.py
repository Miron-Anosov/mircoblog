"""Test valid models."""

import pytest
from pydantic import ValidationError

from src.back_core.validators.valid_user import ValidateUserProfile
from tests.common_data import ValidateUserProfile_fake_user_profile


def test_user_profile_model():
    """Test user model."""
    assert ValidateUserProfile_fake_user_profile.result is True
    assert ValidateUserProfile_fake_user_profile.user.name == "Dick"
    assert len(ValidateUserProfile_fake_user_profile.user.followers) == 1
    assert len(ValidateUserProfile_fake_user_profile.user.following) == 1

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
