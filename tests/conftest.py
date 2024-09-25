"""Conf pytest."""

import httpx
import pytest
import pytest_asyncio
from asgi_lifespan import LifespanManager

from src.core.settings.settings import settings

try:
    assert (
        settings.env_params.MODE == "TEST"
    ), f"Invalid mode: {settings.env_params.MODE}, miss TEST config."
except AssertionError:
    exit(0)


@pytest_asyncio.fixture
async def app():
    """Create app."""
    from src.main import create_app

    async with LifespanManager(create_app()) as manager:
        yield manager.app


@pytest_asyncio.fixture
async def client(app):
    """Create client."""
    async with LifespanManager(app):
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            yield client
