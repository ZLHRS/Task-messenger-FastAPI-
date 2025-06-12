import pytest
from schemes.user_schema import CreateUser
from repository.base_repository import BaseRepository
from models.user_model import User, UserRole


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user_data",
    [
        CreateUser(username="user1", password="password123", email="shaykenov.danialg@gmail.com", role=UserRole("admin")),
        CreateUser(username="user2", password="123sgasd", email="ceburekmaladec@gmail.com", role=UserRole("user")),
    ],
)
async def test_create_serial(db_session, user_data):
    user_repo = BaseRepository(db_session, User)
    created_user = await user_repo.create(user_data)
    assert created_user is not None
    assert created_user.id is not None
    assert created_user.username == user_data.username


@pytest.mark.asyncio
@pytest.mark.parametrize("id_obj", [1, 2, 3])
async def test_get_by_id(db_session, id_obj):
    user_repo = BaseRepository(db_session, User)
    user = await user_repo.get_by_id(id_obj)
    assert user is not None
    assert user.id == id_obj


@pytest.mark.asyncio
async def test_get_all(db_session):
    user_repo = BaseRepository(db_session, User)
    users = await user_repo.get_all()
    assert isinstance(users, list)
    assert len(users) > 0
