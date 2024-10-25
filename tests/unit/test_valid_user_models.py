"""Test valid models_orm."""

import pytest
from pydantic import ValidationError

from src.core.validators.valid_user import (
    ValidateUserProfile,
    ValidModelGetMe,
    ValidUserModel,
)
from tests.common_data import (
    invalid_user_data,
    invalid_user_model,
    invalid_user_profile,
    valid_user_data,
    valid_user_model,
    valid_user_profile,
)


def test_user_profile_model() -> None:
    """Test user model."""
    assert ValidateUserProfile(**valid_user_data)
    user = ValidateUserProfile(**valid_user_data)
    assert user.result is True
    assert user.user.name == "Dick"
    assert len(user.user.followers) == 1
    assert len(user.user.following) == 1

    with pytest.raises(ValidationError):
        ValidateUserProfile(**invalid_user_data)


def test_valid_model_get_me() -> None:
    """Test ValidModelGetMe."""
    assert ValidModelGetMe(**valid_user_profile)
    with pytest.raises(ValidationError):
        ValidModelGetMe(**invalid_user_profile)


def test_valid_user_model() -> None:
    """Test ValidUserModel."""
    assert ValidUserModel(**valid_user_model)
    with pytest.raises(ValidationError):
        ValidUserModel(**invalid_user_model)
