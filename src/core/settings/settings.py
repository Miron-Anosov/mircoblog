"""Configuration .env."""

import os
from abc import abstractmethod
from pathlib import Path

from pydantic import EmailStr, Field, HttpUrl, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict

env = Path(__file__).parent.parent.parent.parent / ".env"
env_test = Path(__file__).parent.parent.parent.parent / ".env.test"


class EnvironmentFileNotFoundError(ValueError):
    """Custom environment exception."""

    pass


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


class InfoSettingEnv(BaseSettings):
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

    model_config = SettingsConfigDict(
        # try to use first test-env if exist else use prod-env
        env_file=env_test if os.path.exists(env_test) else env,
        extra="ignore",
    )


class EnvironmentSettingMix(BaseSettings):
    """EnvironmentSettingMix uses type mode.

    MODE: str : TEST, PROD or something else.
    """

    MODE: str = Field(min_length=2)


class DataBaseEnvConf(UrlDBSettings, EnvironmentSettingMix):
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

    model_config = SettingsConfigDict(
        # try to use first test-env if exist else use prod-env
        env_file=env_test if os.path.exists(env_test) else env,
        extra="ignore",
    )


class AuthJWTEnv(BaseSettings):
    """Class for handling JWT settings.

    Environment Variables:
        - JWT_PRIVATE (str): The private JWT key.
        - JWT_PUBLIC (str): The public JWT key.

    Attributes:
        private (str): The private JWT key.
        public (str): The public JWT key.
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

    private: str = Field()
    public: str = Field()
    algorithm: str = "RS256"
    access_token_expire_minutes: int = Field(default=15)
    refresh_token_expire_days: int = Field(default=30)

    model_config = SettingsConfigDict(
        env_prefix="JWT_",
        extra="ignore",
        env_file=env_test if os.path.exists(env_test) else env,
    )


class RedisEnv(BaseSettings):
    """Class give common environments params.

    Environments params:
     - REDIS_URL: HttpUrl
     - CONTACT_EMAIL: EmailStr
    """

    REDIS_URL: str
    PREFIX: str = "fastapi-cache"

    model_config = SettingsConfigDict(
        # try to use first test-env if exist else use prod-env
        env_file=env_test if os.path.exists(env_test) else env,
        extra="ignore",
    )


class Settings:
    """Common settings for environments.

    Attributes:
        db (DataBaseEnvConf): Environment configuration parameters
            loaded from the `.env` or `.env.test` files.
        jwt_tokens (AuthJWTEnv): JWT configuration including token paths
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
                f"~/.env or ~/.env.test are not exist.\n"
                f"Exist env_test: "
                f"{os.path.exists(env_test)}, path={env_test}\n"
                f"Exist env: "
                f"{os.path.exists(env)}, path={env}\n"
            )
        self.jwt_tokens = AuthJWTEnv()
        self.open_api = InfoSettingEnv()
        self.redis = RedisEnv()


settings = Settings()
