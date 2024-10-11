"""Constants Volumes."""


class JWT:
    """STATIC JWT DATA."""

    DESCRIPTION_PYDANTIC_ACCESS_TOKEN = (
        "Authorization: Bearer JWT access-token. It'll set at "
    )
    DESCRIPTION_PYDANTIC_REFRESH_TOKEN = "Set-cookie: JWT refresh_token"
    DESCRIPTION_PYDANTIC_TOKEN_TYPE = "Bearer"
    DESCRIPTION_PYDANTIC_TITLE = "Token"
    DESCRIPTION_PYDANTIC_EXPIRE_REFRESH = "expires_refresh"
    PAYLOAD_EXPIRE_KEY = "exp"
    PAYLOAD_IAT_KEY = "iat"
    PAYLOAD_SUB_KEY = "sub"
    PAYLOAD_USERNAME_KEY = "username"
    TOKEN_TYPE_FIELD = "type"
    TOKEN_TYPE_ACCESS = "access_token"
    TOKEN_TYPE_REFRESH = "refresh_token"


class MessageError:
    """STATIC ERROR DATA."""

    INVALID_EMAIL_OR_PWD = "Invalid email or password"
    INVALID_TOKEN_ERR = "Invalid token."
    INVALID_TOKEN_ERR_MESSAGE = "Please repeat authentication."
    EMAIL_ALREADY_EXIST = "Email already exist."
    TYPE_ERROR_INVALID_AUTH = "Invalid auth."
    TYPE_ERROR_INTERNAL_SERVER_ERROR = "Internal server error."
    MESSAGE_SERVER_ERROR = "An error occurred."


class TypeEncoding:
    """STATIC ENCODING DATA."""

    UTF8 = "utf-8"


class Headers:
    """STATIC HEADERS DATA."""

    WWW_AUTH_BEARER = {"WWW-Authenticate": "Bearer"}
    WWW_AUTH_BEARER_LOGOUT = {"WWW-Authenticate": 'Bearer realm="logout"'}
    AUTHORIZATION = {"Authorization": ""}
    WWW_AUTH_BEARER_EXPIRED = {
        "WWW-Authenticate": 'Bearer realm="Refresh token expired"'
    }


class PydanticTweets:
    """STATIC PYDANTIC TWEETS."""

    ID_DESCRIPTION = "Unique identifier for the tweet."
    ATTACHMENTS_DESCRIPTION = "List of URLs (optional)"
    TWEET_DATA_DESCRIPTION = "Message to new post"
    TWEET_DATA_MIN_LENGTH_DESCRIPTION = 1
    TWEET_RESULT_BOOL_DESCRIPTION = "Successful or unsuccessful"
    TITLE_TWEET = "Tweet"
    TITLE_GET_TWEETS_RESPONSE = "Get Tweets Response"
    TITLE_TWEETS_RESPONSE = "Tweet Response"
    TITLE_TWEET_REQUEST = "Tweet Request"
    TWEET_MEDIA_IDS_DESCRIPTION = "Array tweet IDs"
    JSON_SCHEMA_TWEET = {
        "example": {
            "result": True,
            "tweets": [
                {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "content": "This is a sample tweet",
                    "attachments": [
                        "/media/images/12345.jpg",
                        "/media/images/12346.jpg",
                    ],
                    "author": {
                        "id": "3fa85f64-4578-4562-b3fc-2c963f66afa6",
                        "name": "Author Name",
                    },
                    "likes": [
                        {
                            "user_id": "3fa85f64-5555-4562-b3fc-2c963f66afa6",
                            "name": "User1",
                        },
                    ],
                },
            ],
        }
    }


class MimeTypes:
    """МIME types constants."""

    APPLICATION_JSON = "application/json"
    MULTIPART_FORM_DATA = "multipart/form-data"


class CacheExpirationTime:
    """REDIS cache expiration times."""

    CACHE_EXPIRATION_TIME_GET_TWEETS = 60
    CACHE_EXPIRATION_TIME_GET_USER = 20


class GunicornConf:
    """Gunicorn conf data."""

    BUILD = "unix:/tmp/gunicorn.sock"
    WSGI_APP = "src.main:create_app()"
    WORKER_CLASS = "uvicorn.workers.UvicornWorker"
    LOG_LEVEL_DEFAULT = "warning"
    ACCESSLOG = "-"
    ERRORLOG = "-"
    TIMEOUT_DEFAULT = 60
