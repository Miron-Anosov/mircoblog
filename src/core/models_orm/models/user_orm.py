"""SQLAlchemy UserORM model."""

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.models_orm.models.base_model import BaseModel

if TYPE_CHECKING:
    from src.core.models_orm.models.auth import UsersAuthORM
    from src.core.models_orm.models.likes_models import LikesORM
    from src.core.models_orm.models.tweet_orm import TweetsORM


class UserORM(BaseModel):
    """User ORM model.

    Table: users
    """

    __tablename__ = "users"
    id: Mapped[UUID] = mapped_column(
        UUID, primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(nullable=False)

    followers: Mapped[list["UserORM"]] = relationship(
        "UserORM",
        secondary="followers",
        primaryjoin="UserORM.id==FollowersORM.following_id",
        secondaryjoin="UserORM.id==FollowersORM.follower_id",
        back_populates="following",
    )
    following: Mapped[list["UserORM"]] = relationship(
        "UserORM",
        secondary="followers",
        primaryjoin="UserORM.id==FollowersORM.follower_id",
        secondaryjoin="UserORM.id==FollowersORM.following_id",
        back_populates="followers",
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
