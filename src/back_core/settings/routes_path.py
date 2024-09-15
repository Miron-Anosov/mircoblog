"""API path."""

ID = "{id}"
# path /api/tweets
TWEETS_PATH = "/tweets"
LIKE = "like"

# path /api/users
USERS_PATH = "/users"  # POST /api/users/<id>/follow
FOLLOW = "follow"


class PathRoutes:
    """Central storage all paths.

    If you need to change a path anywhere, you can do it here.
    """

    PREFIX = "/api"


class TweetsRoutes(PathRoutes):
    """Tweets storage all paths.

    If you need to change a path anywhere, you can do it here.
    """

    TAG = "Tweets"
    TWEETS = f"{TWEETS_PATH}"
    TWEETS_POST_DEL_ID_LIKE = f"{TWEETS_PATH}/{ID}/{LIKE}"
    TWEETS_DEL_BY_ID = f"{TWEETS_PATH}/{ID}"


class UsersRoutes(PathRoutes):
    """Users storage all paths.

    If you need to change a path anywhere, you can do it here.
    """

    TAG = "Users"
    USERS_FOLLOW_BY_ID = f"{USERS_PATH}/{ID}/{FOLLOW}"
    GET_ME = f"{USERS_PATH}/me"
    GET_BY_ID = f"{USERS_PATH}/{ID}"
