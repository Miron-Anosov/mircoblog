"""Test API routes."""

from unittest.mock import patch

from src.back_core.validators.valid_user import ValidateUserProfile
from tests.common_data import user_data


def test_get_user_profile_with_mocked_data_and_api_key():
    """Test func with moke."""
    mocked_profile = ValidateUserProfile(**user_data)
    with patch(
        "src.back_core.controllers.users_controllers.users.get_user_profile",
        return_value=mocked_profile,
    ) as mock_func:
        result = mock_func(api_key="test-key")
        assert result == mocked_profile, f"Validation error: {result}"
