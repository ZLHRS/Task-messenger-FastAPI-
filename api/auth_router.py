from fastapi import APIRouter, Response
from schemes.auth_schema import LoginBase
from use_cases.auth_use_cases import AuthUseCases
from database.db import SessionDep

router = APIRouter(prefix="/auth", tags=["Authorization"])


@router.post("/login")
async def login(response: Response, data: LoginBase, session: SessionDep):
    use_case = AuthUseCases(session)
    return await use_case.login(data, response)


@router.post("/logout")
async def logout(response: Response, session: SessionDep):
    use_case = AuthUseCases(session)
    return await use_case.logout(response)
