"""Core ORM."""

from src.core.models_orm.crud_models.auth_crud import AuthUsers
from src.core.models_orm.crud_models.media_crud import Media
from src.core.models_orm.crud_models.tweet_crud import Tweets
from src.core.models_orm.crud_models.user_crud import Users


class Crud:
    """Combined interface for all CRUD operations."""

    def __init__(
        self,
        tweets_crud: "Tweets",
        user_crud: "Users",
        media_crud: "Media",
        auth_crud: "AuthUsers",
    ) -> None:
        """
        DB worker and crud models.

        db_worker: ManagerDB
        tweets_crud: Tweets()
        user_crud: Users()
        media_crud: Media()
        auth_crud: AuthUsers()
        """
        self.tweets = tweets_crud
        self.users = user_crud
        self.media = media_crud
        self.auth_users = auth_crud


def create_crud_halper() -> Crud:
    """Return CRUD object for all models."""
    create_db = Crud(
        tweets_crud=Tweets(),
        user_crud=Users(),
        media_crud=Media(),
        auth_crud=AuthUsers(),
    )
    return create_db
