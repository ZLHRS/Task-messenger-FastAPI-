from fastapi import Response, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemes.auth_schema import LoginBase
from services.auth_service import AuthService
from utils.security import verify_password, create_access_token
from utils.redis_cashe import delete_from_redis, get_redis


class AuthUseCases:
    def __init__(self, db: AsyncSession):
        self.auth_service = AuthService(db)

    async def login(self, data: LoginBase, response: Response):
        token_redis = await get_redis("my_token")
        if token_redis:
            raise HTTPException(
                status_code=401, detail="You are already logged in to your account."
            )
        user = await self.auth_service.find_username(data.username)
        if not user or not verify_password(data.password, user.password):
            raise HTTPException(status_code=401, detail="Invalid username or password")
        access_token = create_access_token(
            {
                "user_id": user.id,
                "sub": user.username,
                "email": user.email,
                "role": user.role.value,
            }
        )
        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            secure=False,
            samesite="lax",
            max_age=1800,
        )
        await self.auth_service.token_redis("my_token", access_token)
        await self.auth_service.token_redis("my_email", user.email)
        return {"token": access_token}

    @staticmethod
    async def logout(response: Response):
        response.set_cookie(
            key="access_token", value="", httponly=True, samesite="lax", expires=0
        )
        await delete_from_redis("my_token")
        return {"message": "Logged out successfully"}
