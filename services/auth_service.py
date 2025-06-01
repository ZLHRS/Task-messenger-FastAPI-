from sqlalchemy.ext.asyncio import AsyncSession
from repository.auth_repository import AuthRepository
from utils.redis_cashe import get_or_set


class AuthService:
    def __init__(self, db: AsyncSession):
        self.auth_repo = AuthRepository(db)

    async def find_username(self, username: str):
        return await self.auth_repo.find_username(username)

    @staticmethod
    async def token_redis(key, token):
        return await get_or_set(key, 300, token)
