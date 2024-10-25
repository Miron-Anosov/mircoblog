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

    CREATE TABLE followers (
        id SERIAL NOT NULL,
        follower_id UUID NOT NULL,
        followed_id UUID NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(follower_id) REFERENCES users (id),
        FOREIGN KEY(followed_id) REFERENCES users (id)
    )

    """

    __tablename__ = "followers"
    __mapper_args__ = {"eager_defaults": True}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    follower_id: Mapped[str] = mapped_column(UUID, ForeignKey("users.id"))
    followed_id: Mapped[str] = mapped_column(UUID, ForeignKey("users.id"))
    follower: Mapped["UserORM"] = relationship(
        "UserORM", foreign_keys=[follower_id], back_populates="followers"
    )

    following: Mapped["UserORM"] = relationship(
        "UserORM", foreign_keys=[followed_id], back_populates="following"
    )
