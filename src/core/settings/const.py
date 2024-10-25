"""Constants Volumes."""

from pathlib import Path

from src.core.settings.routes_path import TweetsRoutes


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


class CommonConfSettings:
    """Common configurate."""

    ENV_FILE_NAME = ".env"
    ENV_TEST_FILE_NAME = ".env.test"
    EXTRA_IGNORE = "ignore"

    ENV = Path(__file__).parent.parent.parent.parent / ENV_FILE_NAME

    ENV_TEST = Path(__file__).parent.parent.parent.parent / ENV_TEST_FILE_NAME


class MessageError:
    """STATIC ERROR DATA."""

    INVALID_EMAIL_OR_PWD = "Invalid email or password"
    INVALID_TOKEN_ERR = "Invalid token."
    INVALID_ID_ERR = "Invalid ID."
    INVALID_ID_ERR_MESSAGE = "Type ID is not correct."
    INVALID_ID_ERR_MESSAGE_404 = "ID is not exist."
    INVALID_TOKEN_ERR_MESSAGE = "Please repeat authentication."
    EMAIL_ALREADY_EXIST = "Email already exist."
    TYPE_ERROR_INVALID_AUTH = "Invalid auth."
    TYPE_ERROR_INTERNAL_SERVER_ERROR = "Internal server error."
    TYPE_ERROR_404 = "HTTP_404_NOT_FOUND"
    TYPE_ERROR_500 = "HTTP_500_INTERNAL_SERVER_ERROR"
    MESSAGE_SERVER_ERROR = "An error occurred."
    MESSAGE_ENV_FILE_INCORRECT_OR_NOT_EXIST = (
        "~/.env or ~/.env.test incorrect or not exist"
    )
    MESSAGE_USER_NOT_FOUND = "User not found"


class TypeEncoding:
    """STATIC ENCODING DATA."""

    UTF8 = "utf-8"


class JWTconf:
    """Conf for settings."""

    ALGORITHM = "RS256"
    ENV_PREFIX = "JWT_"
    ACCESS_EXPIRE_MINUTES = 15
    REFRESH_EXPIRE_DAYS = 30


class Headers:
    """STATIC HEADERS DATA."""

    WWW_AUTH_BEARER = {"WWW-Authenticate": "Bearer"}
    WWW_AUTH_BEARER_LOGOUT = {"WWW-Authenticate": 'Bearer realm="logout"'}
    AUTHORIZATION = {"Authorization": ""}
    WWW_AUTH_BEARER_EXPIRED = {
        "WWW-Authenticate": 'Bearer realm="Refresh token expired"'
    }
    CACHE_CONTROL = "Cache-Control"
    CACHE_MAX_AGE = "max-age="
    ETAG = "ETag"
    X_CACHE = "X-Cache"
    X_CACHE_MISS = "MISS"
    X_CACHE_HIT = "HIT"
    IF_NONE_MATCH = "if-none-match"


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


class PydanticUser:
    """Swagger Docs User model."""

    TITLE_SWAGGER = "User"
    DESCRIPTION_ID = "Author's unique ID"
    DESCRIPTION_NAME = "Author's name"
    TITLE = "User's profile"
    JSON_SCHEMA_USER = {
        "example": {
            "result": True,
            "user": {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "name": "Dick",
                "followers": [
                    {
                        "id": "3fa33364-5717-4562-b3fc-2c963f66afa6",
                        "name": "Tom",
                    }
                ],
                "following": [
                    {
                        "id": "3fa33364-5717-4562-b3fc-2c963f4563fa",
                        "name": "Ramil",
                    }
                ],
            },
        }
    }


class DetailError:
    """Default Error model to response."""

    content = {
        "application/json": {
            "example": {
                "detail": {
                    "result": False,
                    "error_type": "String",
                    "error_message": "String",
                }
            }
        }
    }


class ResponseError:
    """Swagger Docs Errors."""

    responses = {
        401: {
            "description": "Invalid credentials",
            "content": DetailError.content,
        },
        403: {"description": "Forbidden", "content": DetailError.content},
        404: {"description": "Not Found", "content": DetailError.content},
        422: {
            "description": "Validation Error",
            "content": DetailError.content,
        },
        500: {
            "description": "Invalid credentials",
            "content": DetailError.content,
        },
    }


class ResponsesUsersError:
    """Swagger Docs Get Tweets."""


class ResponsesGetTweets:
    """Swagger Docs Get Tweets."""

    responses_304 = {
        304: {"description": "Not Modified", "content": {}},
    }

    copy_resp = ResponseError.responses.copy()
    copy_resp.update(responses_304)
    copy_resp.pop(401)
    copy_resp.pop(403)
    responses = copy_resp


class ResponsesAuthUser:
    """Swagger Docs."""

    responses = dict()
    responses[401] = ResponseError.responses.get(401)
    responses[500] = ResponseError.responses.get(500)


class Response500:
    """Swagger Docs."""

    responses = dict()
    responses[500] = ResponseError.responses.get(500)


class ResponsesAuthNewUser:
    """Swagger Docs."""

    responses = dict()
    responses[500] = ResponseError.responses.get(500)
    responses[422] = ResponseError.responses.get(422)


class MimeTypes:
    """МIME types constants."""

    APPLICATION_JSON = "application/json"
    MULTIPART_FORM_DATA = "multipart/form-data"


class CacheConf:
    """REDIS cache expiration times."""

    CACHE_EXPIRATION_TIME_GET_TWEETS = 60
    CACHE_EXPIRATION_TIME_GET_USER = 20
    PREFIX_GET_TWEETS = f"GET {TweetsRoutes.PREFIX}{TweetsRoutes.TWEETS}"
    PREFIX_USER_BY_ID = "GET api/user/id"
    PREFIX_USER_ME = "GET api/user/me"


class GunicornConf:
    """Gunicorn conf data."""

    BUILD = "unix:/tmp/gunicorn.sock"
    WSGI_APP = "src.main:create_app()"
    WORKER_CLASS = "uvicorn.workers.UvicornWorker"
    LOG_LEVEL_DEFAULT = "warning"
    ACCESSLOG = "-"
    ERRORLOG = "-"
    TIMEOUT_DEFAULT = 60
    MIN_WORKERS = 1


class RedisConf:
    """Redis conf data."""

    PREFIX = "microblog-api"
    MIN_LENGTH_PREFIX = 3
    DEFAULT_PORT = 6379
    REDIS_DB = 0
    REDIS_USER = "default"


class Keys:
    """KEYS."""

    REQUEST = "request"
    RESPONSE = "response"
    GET = "GET"
