"""SQLAlchemy engine."""

from abc import ABC, abstractmethod
from asyncio import current_task
from typing import Optional

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)

from src.core.models_orm.models.auth import UsersAuthORM
from src.core.models_orm.models.base_model import BaseModel
from src.core.models_orm.models.followers_orm import FollowersORM
from src.core.models_orm.models.likes_models import LikesORM
from src.core.models_orm.models.media_orm import MediaORM
from src.core.models_orm.models.tweet_orm import TweetsORM
from src.core.models_orm.models.user_orm import UserORM
from src.core.models_orm.models.users_auth_ip import UsersAuthIPORM


class EngineCreator(ABC):
    """Abstract method create_async_engine."""

    @abstractmethod
    def create_async_engine(self, *args, **kwargs) -> "AsyncEngine":
        """Create async engine."""
        pass


class SessionCreator(ABC):
    """Abstract method create_session."""

    @abstractmethod
    def create_session(
        self, *args, **kwargs
    ) -> "async_sessionmaker[AsyncSession]":
        """Create async engine."""
        pass


class ScopedSessionManager(ABC):
    """Abstract method get_scoped_session."""

    @abstractmethod
    def get_scoped_session(self) -> "AsyncSession":
        """Return AsyncSession from current scoped."""
        pass


class CreatorBDInterface(ABC):
    """Abstract DB creator."""

    @abstractmethod
    async def create_tables(self):
        """Create table if not exist."""
        pass


class ManagerDBInterface(
    EngineCreator,
    SessionCreator,
    ScopedSessionManager,
    CreatorBDInterface,
    ABC,
):
    """Abstract Interface."""

    """API DB."""

    @abstractmethod
    def create_session(
        self, engine: AsyncEngine
    ) -> "async_sessionmaker[AsyncSession]":
        """Create db session."""
        pass

    @abstractmethod
    def get_scoped_session(self) -> "AsyncSession":
        """Return current scope."""
        pass

    @abstractmethod
    def create_async_engine(self) -> "AsyncEngine":
        """Create async engine."""
        pass

    @abstractmethod
    async def create_tables(self):
        """Create tables."""
        pass


class AsyncEngineCreator(EngineCreator):
    """Crete async db engine."""

    def create_async_engine(self, url: str, echo: bool) -> AsyncEngine:
        """Return AsyncEngine."""
        # TODO: add logger DEBUG
        return create_async_engine(url=url, echo=echo, pool_pre_ping=True)


class AsyncSessionCreator(SessionCreator):
    """Create async session."""

    def create_session(
        self, engine: AsyncEngine
    ) -> async_sessionmaker[AsyncSession]:
        """Return session maker with config.

        Args:
                engine: (AsyncEngine): Default SQLAlchemy engine.

        Conf:
                - expire_on_commit=False
                - autoflush=False
                - autocommit=False
                - class_=AsyncSession

        Return:
                - sync_sessionmaker[AsyncSession]: SQLAlchemy AsyncSession.
        """
        return async_sessionmaker(
            bind=engine,
            expire_on_commit=False,
            autoflush=False,
            autocommit=False,
            class_=AsyncSession,
        )


class AsyncScopedSessionManager(ScopedSessionManager):
    """Return current scope session."""

    def __init__(self, session_maker: async_sessionmaker[AsyncSession]):
        """Init session scope."""
        self.async_scoped_session = async_scoped_session(
            session_factory=session_maker, scopefunc=current_task
        )

    def get_scoped_session(self) -> AsyncSession:
        """Return current scope."""
        return self.async_scoped_session()


class ManagerDB(ManagerDBInterface):
    """Async engine manager."""

    _instance: Optional["ManagerDBInterface"] = None

    def __new__(cls, *args, **kwargs):
        """Create singleton API."""
        if cls._instance is None:
            # todo: add logger
            cls._instance = super(ManagerDB, cls).__new__(cls)
        return cls._instance

    def __init__(self, url: str, echo: bool) -> "None":
        """Init SQLAlchemy manager."""
        if not hasattr(self, "_initialize_tables"):
            self.__url = url
            self.__echo = echo
            self._engine_creator = AsyncEngineCreator()
            self._async_session_maker = AsyncSessionCreator()
            self.async_engine = self.create_async_engine()
            self._session = self.create_session(self.async_engine)
            self._async_scoped_session = AsyncScopedSessionManager(
                self._session
            )

            self._initialize_tables = False

    def create_session(
        self, engine: "AsyncEngine"
    ) -> "async_sessionmaker[AsyncSession]":
        """Create db session."""
        # TODO: add logger about new session DEBUG
        return self._async_session_maker.create_session(engine=engine)

    def get_scoped_session(self) -> "AsyncSession":
        """Return current scope."""
        return self._async_scoped_session.get_scoped_session()

    def create_async_engine(self) -> "AsyncEngine":
        """Create async engine."""
        return self._engine_creator.create_async_engine(
            url=self.__url, echo=self.__echo
        )

    async def initialize(self):
        """Initialize the database by creating tables."""
        if self._initialize_tables is False:
            await self.create_tables()
            self._initialize_tables = True

    async def create_tables(self):
        """Create table if not exist."""
        async with self.async_engine.begin() as conn:
            # todo: add logger INIT DB TABLES
            await conn.run_sync(BaseModel.metadata.create_all)


async def get_engine(url: str, echo: bool) -> "ManagerDB":
    """Create ORM session/engine manager."""
    manager = ManagerDB(url=url, echo=echo)
    await manager.initialize()
    return manager
