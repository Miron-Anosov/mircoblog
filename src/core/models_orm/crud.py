"""
Core ORM module.

This module provides a combined interface for handling CRUD operations
across multiple models. It simplifies access to CRUD functionality by
grouping operations for tweets, users, media, and authentication under
a single class, `Crud`.

Classes:
    Crud: Combines CRUD operations for tweets, users, media, and auth.

Functions:
    create_crud_helper: Creates and returns a `Crud` instance.
"""

from src.core.models_orm.crud_models.auth_crud import AuthUsers
from src.core.models_orm.crud_models.media_crud import Media
from src.core.models_orm.crud_models.tweet_crud import Tweets
from src.core.models_orm.crud_models.user_crud import Users


class Crud:
    """Combined interface for all CRUD operations.

    Attributes:
        tweets: CRUD operations for tweet model.
        users: CRUD operations for user model.
        media: CRUD operations for media model.
        auth_users: CRUD operations for auth model.
    """

    def __init__(
        self,
        tweets_crud: "Tweets",
        user_crud: "Users",
        media_crud: "Media",
        auth_crud: "AuthUsers",
    ) -> None:
        """
        Initialize Crud with specific CRUD instances.

        Args:
            tweets_crud: Instance of Tweets CRUD.
            user_crud: Instance of Users CRUD.
            media_crud: Instance of Media CRUD.
            auth_crud: Instance of AuthUsers CRUD.
        """
        self.tweets = tweets_crud
        self.users = user_crud
        self.media = media_crud
        self.auth_users = auth_crud


def create_crud_helper() -> Crud:
    """Create and return a Crud object for all models.

    Returns:
        Crud: An instance of the Crud class with initialized models.
    """
    create_db = Crud(
        tweets_crud=Tweets(),
        user_crud=Users(),
        media_crud=Media(),
        auth_crud=AuthUsers(),
    )
    return create_db
