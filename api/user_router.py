from fastapi import APIRouter
from fastapi.params import Depends
from core.dependencies import get_current_admin
from schemes.user_schema import CreateUser, UserSchema, UserUpdateRole
from use_cases.user_use_cases import UserUseCase
from typing import List
from database.db import SessionDep

router = APIRouter(prefix="/user", dependencies=[Depends(get_current_admin)])


@router.get("/all", response_model=List[UserSchema], tags=["Admin Panel"])
async def show_users(session: SessionDep):
    use_case = UserUseCase(session)
    return await use_case.show_all()


@router.post("/new", response_model=UserSchema, tags=["Admin Panel"])
async def register_user(user_data: CreateUser, session: SessionDep):
    use_case = UserUseCase(session)
    return await use_case.create_user(user_data)


@router.patch("", response_model=UserSchema, tags=["Admin Panel"])
async def upgrade_downgrade(
    user_id: int, update_role: UserUpdateRole, session: SessionDep
):
    use_case = UserUseCase(session)
    return await use_case.upgrade_downgrade(user_id, update_role)
