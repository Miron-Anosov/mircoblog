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


@pytest.mark.asyncio
async def test_get_user_profile_with_invalid_api_key(client: AsyncClient):
    """Test GET /users/me without headers : api-key."""
    with patch(
        "src.back_core.controllers.users_controllers.users.api_key_depend",
        return_value=None,
    ):
        invalid_api_key = {"api-key": "test"}
        response = await client.get(
            f"{UsersRoutes.PREFIX}{UsersRoutes.GET_ME}",
            headers=invalid_api_key,
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST


# @pytest.mark.asyncio
# async def test_get_user_profile_with_valid_api_key(client: AsyncClient):
#     """Test GET /users/me without headers : api-key."""
#     with patch(
#             "src.back_core.controllers.users_controllers.users.api_key_depend",
#             return_value=None,
#     ):
#         api_key = {"api-key": "test-api-key"}
#         response = await client.get(
#             f"{UsersRoutes.PREFIX}{UsersRoutes.GET_ME}",
#             headers=api_key
#         )
#         assert response.status_code == status.HTTP_200_OK
