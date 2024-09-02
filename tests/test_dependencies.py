"""Tests developers dependencies."""

import pytest

from src.settings.settings import CommonSettings, settings

# import httpx
# import pytest_asyncio
# from asgi_lifespan import LifespanManager
# from httpx import codes


@pytest.mark.test_config
def test_dependencies_installed():
    """Test env config."""
    assert settings.test.ECHO_TEST is False


@pytest.mark.test_config
def test_dependencies_installed_1():
    """Test env config."""
    assert settings.test.get_url_database


@pytest.mark.test_config
def test_dependencies_installed_2():
    """Test env config."""
    with pytest.raises(TypeError):
        _ = CommonSettings().get_url_database
