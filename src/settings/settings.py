"""Configuration .env."""

from abc import abstractmethod
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class CommonSettings(BaseSettings):
    """Common config model for environments."""

    @property
    @abstractmethod
    def get_url_database(self) -> str:
        """Return database URL."""
        raise NotImplementedError("Method must be overridden in subclasses.")


class ProdSettings(CommonSettings):
    """Production environments are deploy."""

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
        env_file=Path(__file__).parent.parent.parent / ".env", extra="ignore"
    )


class TestSettings(CommonSettings):
    """Test environments are test."""

    POSTGRES_HOST_TEST: str
    POSTGRES_PORT_TEST: int
    POSTGRES_USER_TEST: str
    POSTGRES_DB_TEST: str
    POSTGRES_PASSWORD_TEST: str
    ECHO_TEST: bool

    @property
    def get_url_database(self) -> str:
        """Return database URL."""
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER_TEST}:"
            f"{self.POSTGRES_PASSWORD_TEST}@{self.POSTGRES_HOST_TEST}:"
            f"{self.POSTGRES_PORT_TEST}/{self.POSTGRES_DB_TEST}"
        )

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent.parent / ".env.test",
        extra="ignore",
    )


class Settings:
    """Common settings for environments."""

    @property
    def prod(self) -> ProdSettings:
        """Use production env."""
        return ProdSettings()

    @property
    def test(self) -> TestSettings:
        """Use test env.test."""
        return TestSettings()


settings = Settings()
