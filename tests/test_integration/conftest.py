from config import DataBaseConfig
from database.db import Base, engine, session_local
import pytest
from schemes.user_schema import CreateUser
from repository.base_repository import BaseRepository
from models.user_model import User, UserRole


@pytest.fixture(scope="session", autouse=True)
async def setup_database():
    assert DataBaseConfig.db == "mydatabase_test"
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture
async def db_session():
    async with session_local() as session:
        yield session
        await session.rollback()


@pytest.fixture
async def setup_users(db_session):
    user_repo = BaseRepository(db_session, User)
    test_users = [
        CreateUser(username="user1", password="password123", role=UserRole("admin")),
        CreateUser(username="user2", password="123sgasd", role=UserRole("user")),
        CreateUser(username="user3", password="asasdd", role=UserRole("admin")),
    ]
    for user_data in test_users:
        await user_repo.create(user_data)
    await db_session.commit()
    yield
    await db_session.rollback()
