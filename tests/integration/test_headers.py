"""Headers integration tests API."""

from unittest.mock import patch

import pytest
from fastapi import status
from httpx import AsyncClient

from src.back_core.settings.routes_path import UsersRoutes
from src.back_core.validators.valid_user import ValidateUserProfile
from tests.common_data import user_data


@pytest.mark.asyncio
async def test_get_user_profile_without_api_key(client: AsyncClient):
    """Test GET /users/me without headers : api-key."""
    with patch(
        "src.back_core.controllers.users_controllers.users.api_key_depend",
        return_value=None,
    ):
        response = await client.get(
            f"{UsersRoutes.PREFIX}{UsersRoutes.GET_ME}"
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
