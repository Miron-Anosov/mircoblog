"""Configuration .env."""

import os
from abc import abstractmethod
from multiprocessing import cpu_count

from pydantic import EmailStr, Field, HttpUrl, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.core.settings.const import (
    CommonConfSettings,
    GunicornConf,
    JWTconf,
    MessageError,
    RedisConf,
)


class EnvironmentFileNotFoundError(ValueError):
    """Custom environment exception."""

    pass


class EnvironmentSetting(BaseSettings):
    """EnvironmentSettingMix uses type mode.

    SettingsConfigDict: dict : TEST, PROD env.
    """

    model_config = SettingsConfigDict(
        # try to use first test-env if exist else use prod-env
        env_file=(
            CommonConfSettings.ENV_TEST
            if os.path.exists(CommonConfSettings.ENV_TEST)
            else CommonConfSettings.ENV
        ),
        extra=CommonConfSettings.EXTRA_IGNORE,
    )


class UrlDBSettings(BaseSettings):
    """Common config model for environments.

    Methods:
        get_url_database(self) -> str

    Raise:
        - NotImplementedError: Method must be overridden in subclasses.
    """

    @property
    @abstractmethod
    def get_url_database(self) -> str:
        """Return database URL."""
        raise NotImplementedError("Method must be overridden in subclasses.")


class InfoSettingEnv(EnvironmentSetting):
    """Class give common environments params.

    Environments params:
     - VERSION_API: str
     - CONTACT_NAME: str
     - CONTACT_URL: HttpUrl
     - CONTACT_EMAIL: EmailStr
    """

    VERSION_API: str = Field(min_length=5, max_length=8)
    CONTACT_NAME: str = Field(min_length=2, max_length=15)
    CONTACT_URL: HttpUrl
    CONTACT_EMAIL: EmailStr


class DataBaseEnvConf(UrlDBSettings, EnvironmentSetting):
    """Configuration for production environments.

    Attributes:
        POSTGRES_HOST (str): The hostname of the PostgreSQL server.
        POSTGRES_PORT (int): The port number for PostgreSQL.
        POSTGRES_USER (str): The username for connecting to PostgreSQL.
        POSTGRES_DB (str): The name of the PostgreSQL database.
        POSTGRES_PASSWORD (str): The password for the PostgreSQL user.
        ECHO (bool): A flag to enable or disable SQLAlchemy query logging.
    """

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_PASSWORD: str
    ECHO: bool
    POOL_TIMEOUT: int
    POOL_SIZE_SQL_ALCHEMY_CONF: int
    MAX_OVERFLOW: int
    MODE: str = Field(min_length=2)

    @property
    def get_url_database(self) -> str:
        """Return the database URL for SQLAlchemy.

        Constructs and returns a PostgreSQL URL using the asyncpg driver
        to be used by SQLAlchemy for database connections.

        Returns:
            str: The full database connection URL.
        """
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


class AuthJWTEnv(EnvironmentSetting):
    """Class for handling JWT settings.

    Environment Variables:
        - JWT_PRIVATE (str): The private JWT key.
        - JWT_PUBLIC (str): The public JWT key.

    Attributes:
        jwt_private (str): The private JWT key.
        jwt_public (str): The public JWT key.
        algorithm (str): The algorithm used for JWT encryption,
            default is 'RS256'.
        access_token_expire_minutes (int): The expiration time for the
            access token in minutes, default is 15.
        refresh_token_expire_days (int): The expiration time for the
            refresh token in days, default is 30.

    Example:
        Usage of the class to load JWT configuration from an `.env` file:

        ```python
        auth_settings = AuthJWT()
        print(auth_settings.private)
        print(auth_settings.public)
        ```

    Configuration:
        - env_prefix: Prefix for environment variables, used to load the
            `JWT_PRIVATE` and `JWT_PUBLIC` variables.
        - extra: Ignores extra variables not specified in the model.
        - env_file: Loads environment variables from `.env.test` if it
            exists, otherwise from `.env`.
    """

    jwt_private: str = Field()
    jwt_public: str = Field()
    algorithm: str = JWTconf.ALGORITHM
    access_token_expire_minutes: int = Field(
        default=JWTconf.ACCESS_EXPIRE_MINUTES
    )
    refresh_token_expire_days: int = Field(default=JWTconf.REFRESH_EXPIRE_DAYS)


class RedisEnv(EnvironmentSetting):
    """Class give common environments params.

    Environments params:
     - REDIS_URL: HttpUrl
     - CONTACT_EMAIL: EmailStr
    """

    REDIS_URL: str
    REDIS_PASSWORD: str
    REDIS_PREFIX: str = Field(
        default=RedisConf.PREFIX, min_length=RedisConf.MIN_LENGTH_PREFIX
    )


class GunicornENV(EnvironmentSetting):
    """Conf Gunicorn."""

    WORKERS: int = Field(default=cpu_count(), ge=GunicornConf.MIN_WORKERS)
    BUILD: str = Field(default=GunicornConf.BUILD)
    LOG_LEVEL: str = Field(default=GunicornConf.LOG_LEVEL_DEFAULT)
    WSGI_APP: str = Field(default=GunicornConf.WSGI_APP)
    WORKER_CLASS: str = Field(default=GunicornConf.WORKER_CLASS)
    TIMEOUT: int = Field(default=GunicornConf.TIMEOUT_DEFAULT)
    ACCESSLOG: str = Field(default=GunicornConf.ACCESSLOG)
    ERRORLOG: str = Field(default=GunicornConf.ERRORLOG)


class Settings:
    """Common settings for environments.

    Attributes:
        db (DataBaseEnvConf): Environment configuration parameters
            loaded from the `.env` or `.env.test` files.
        jwt (AuthJWTEnv): JWT configuration including token paths
            and expiration settings.
        open_api (InfoSettingEnv): OpenApi docs

    Raises:
        EnvironmentFileNotFoundError: If neither the `.env` nor the
            `.env.test` files are found, this error is raised with
            detailed information about the missing files.
    """

    def __init__(self) -> None:
        """Initialize the settings by loading environment variables.

        Tries to load the environment parameters using `EnvConf`. If the
        `.env` or `.env.test` files are not found, an exception is
        raised indicating which files were missing.
        """
        try:
            self.db = DataBaseEnvConf()
        except ValidationError:
            raise EnvironmentFileNotFoundError(
                MessageError.MESSAGE_ENV_FILE_INCORRECT_OR_NOT_EXIST
            )
        self.jwt = AuthJWTEnv()
        self.open_api = InfoSettingEnv()
        self.redis = RedisEnv()
        self.gunicorn = GunicornENV()


settings = Settings()
print(settings.gunicorn.WORKERS)
