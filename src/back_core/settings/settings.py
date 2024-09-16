"""Configuration .env."""

import os
from abc import abstractmethod
from pathlib import Path

from pydantic import EmailStr, Field, HttpUrl, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict

env = Path(__file__).parent.parent.parent.parent / ".env"
env_test = Path(__file__).parent.parent.parent.parent / ".env.test"


class RequirementsEnvironmentFileNotFound(ValueError):
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
        env_file=env_test if os.path.exists(env_test) else env,
        extra="ignore",
    )


class Settings:
    """Common settings for environments."""

    def __init__(self) -> None:
        """Interface for environments."""
        try:
            self.env_params = EnvConf()
        except ValidationError:
            raise RequirementsEnvironmentFileNotFound(
                f"~/.env or ~/.env.test are not exist.\n"
                f"Exist env_test: "
                f"{os.path.exists(env_test)}, path={env_test}\n"
                f"Exist env: "
                f"{os.path.exists(env)}, path={env}\n"
            )


print(env_test if os.path.exists(env_test) else env)
settings = Settings()
