from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.user_model import User


class AuthRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def find_username(self, username: str):
        res = await self.db.execute(select(User).where(User.username == username))
        return res.scalar_one_or_none()
