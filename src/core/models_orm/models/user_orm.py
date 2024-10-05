"""SQLAlchemy UserORM model."""

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.models_orm.models.base_model import BaseModel

if TYPE_CHECKING:
    from src.core.models_orm.models.auth import UsersAuthORM
    from src.core.models_orm.models.followers_orm import FollowersORM
    from src.core.models_orm.models.likes_models import LikesORM
    from src.core.models_orm.models.tweet_orm import TweetsORM


class UserORM(BaseModel):
    """User ORM model.

    Table: users

        CREATE TABLE users (
        id UUID NOT NULL,
        name VARCHAR NOT NULL,
        PRIMARY KEY (id)
    )
    """

    __tablename__ = "users"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    followers: Mapped[list["FollowersORM"]] = relationship(
        "FollowersORM",
        foreign_keys="[FollowersORM.followed_id]",
        back_populates="following",
        cascade="all, delete-orphan",
    )

    following: Mapped[list["FollowersORM"]] = relationship(
        "FollowersORM",
        foreign_keys="[FollowersORM.follower_id]",
        back_populates="follower",
        cascade="all, delete-orphan",
    )

    users_profile: Mapped["UsersAuthORM"] = relationship(
        "UsersAuthORM", back_populates="user_auth"
    )
    likes: Mapped[list["LikesORM"]] = relationship(
        "LikesORM",
        back_populates="user",
    )

    tweets: Mapped[list["TweetsORM"]] = relationship(
        back_populates="owner",
    )
