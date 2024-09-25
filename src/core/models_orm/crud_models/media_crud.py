"""Crud worker for db."""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.core.models_orm.models.media_orm import MediaORM


class _MediaInterface(ABC):
    """Interface for media-related operations."""

    @staticmethod
    @abstractmethod
    async def post_img(link: str) -> str:
        """Upload image and return its link."""
        return ""  # TODO: miss to make logic


class Media(_MediaInterface):
    """Media CRUD methods."""

    @staticmethod
    async def post_img(link: str) -> str:
        """Upload image and return its link."""
        return ""  # TODO: miss to make logic
