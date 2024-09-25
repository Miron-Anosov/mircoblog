"""SQLAlchemy FollowersORM model."""

from typing import TYPE_CHECKING

from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.models_orm.models.base_model import BaseModel

if TYPE_CHECKING:
    from src.core.models_orm.models.user_orm import UserORM


class FollowersORM(BaseModel):
    """Followers ORM model.

    Table: followers
    """

    __tablename__ = "followers"
    __mapper_args__ = {"eager_defaults": True}
    follower_id: Mapped[str] = mapped_column(
        UUID, ForeignKey("users.id"), primary_key=True
    )
    following_id: Mapped[str] = mapped_column(
        UUID, ForeignKey("users.id"), primary_key=True
    )
