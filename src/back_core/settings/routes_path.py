"""API path."""

import enum

# path /api/tweets
TWEETS_PATH = "/tweets"
TWEET_ID = "{tweet_id}"
LIKE = "like"

# path /api/users
USERS_PATH = "/users"  # POST /api/users/<id>/follow
USER_ID = "{id}"
FOLLOW = "follow"


class PathRoutes(enum.Enum):
    """Central storage all paths.

    If you need to change a path anywhere, you can do it here.
    """

    PREFIX = "/api"
    TWEETS = f"{TWEETS_PATH}"
    TWEETS_POST_DEL_ID_LIKE = f"{TWEETS_PATH}/{TWEET_ID}/{LIKE}"
    TWEETS_DEL_BY_ID = f"{TWEETS_PATH}/{TWEET_ID}"
    USERS_FOLLOW_BY_ID = f"{USERS_PATH}/{USER_ID}/{FOLLOW}"
