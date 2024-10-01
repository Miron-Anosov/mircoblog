"""Configuration .env."""

import os
from abc import abstractmethod
from pathlib import Path

from pydantic import EmailStr, Field, HttpUrl, ValidationError, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

env = Path(__file__).parent.parent.parent.parent / ".env"
env_test = Path(__file__).parent.parent.parent.parent / ".env.test"


class EnvironmentFileNotFoundError(ValueError):
    """Custom environment exception."""

    pass


class CommonSettings(BaseSettings):
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


class InfoSettingMix(BaseSettings):
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


class EnvironmentSettingMix(BaseSettings):
    """EnvironmentSettingMix uses type mode.

    MODE: str : TEST, PROD or something else.
    """

    MODE: str = Field(min_length=2)


class EnvConf(CommonSettings, InfoSettingMix, EnvironmentSettingMix):
    """Production environments are deploy.

    Environments params:
     - POSTGRES_HOST: str
     - POSTGRES_PORT: int
     - POSTGRES_USER: str
     - POSTGRES_DB: str
     - POSTGRES_PASSWORD: str
     - ECHO: bool
    """

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_PASSWORD: str
    ECHO: bool

    @property
    def get_url_database(self) -> str:
        """Return database URL."""
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


def default_token_path(token_type: str) -> Path:
    """Return path for tokens."""
    return Path(__file__).parent.parent.parent / f"certs/jwt-{token_type}.pem"


class AuthJWT(BaseSettings):
    """AuthJWT token path with fallback to environment variables."""

    private_token: Path = Field(
        default_factory=lambda: default_token_path("private")
    )
    public_token: Path = Field(
        default_factory=lambda: default_token_path("public"),
    )
    algorithm: str = "RS256"
    access_token_expire_minutes: int = Field(default=15)
    refresh_token_expire_days: int = Field(default=30)

    @classmethod
    @field_validator("private_token", "public_token")
    def validate_token_paths(cls, value, info):
        """Validate openssl data."""
        if value.exists():
            return value

        env_var_name = f"JWT_{info.field_name.split('_')[0].upper()}_KEY_PATH"
        env_path = os.getenv(env_var_name)

        if env_path and Path(env_path).exists():
            return Path(env_path)

        raise EnvironmentFileNotFoundError(
            f"No valid path found for {info.field_name}. "
            f"Tried default path: {value} and "
            f"environment variable: {env_var_name}"
        )

    model_config = SettingsConfigDict(validate_assignment=True)


class Settings:
    """Common settings for environments."""

    def __init__(self) -> None:
        """Interface for environments."""
        try:
            self.env_params = EnvConf()
        except ValidationError:
            raise EnvironmentFileNotFoundError(
                f"~/.env or ~/.env.test are not exist.\n"
                f"Exist env_test: "
                f"{os.path.exists(env_test)}, path={env_test}\n"
                f"Exist env: "
                f"{os.path.exists(env)}, path={env}\n"
            )
        self.jwt_tokens = AuthJWT()


settings = Settings()
