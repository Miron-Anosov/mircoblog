"""API path."""

import enum


class PathRoutes(enum.Enum):
    """Central storage all paths.

    If you need to change a path anywhere, you can do it here.
    """

    PREFIX = "/api"
    TWEETS = "/tweets"
    TWEETS_ID_LIKE = "/tweets/{tweet_id}/like"
    TWEETS_DEL_BY_ID = "/tweets/{tweet_id}"
    TWEETS_DEL_LIKE_BY_ID = "/tweets/{tweet_id}/like"
    USERS = "/users"
