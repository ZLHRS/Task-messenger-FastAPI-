from typing import Union
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemes.task_schema import CreateTask, PatchTask, TaskUpdateStatus
from services.task_service import TaskService
from utils.celery_app import send_email_async


class TaskUseCase:
    def __init__(self, db: AsyncSession):
        self.task_service = TaskService(db)

    async def create_task(self, data: CreateTask):
        result = await self.task_service.create_task(data)
        await self.task_service.update_redis("tasks:all")
        data_dict = data.model_dump()
        user_id = data_dict.get("user_id")
        user_data = await self.task_service.get_user_by_id(user_id)
        send_email_async.delay(user_data.email, "New Task", "Please complete your task")
        return result

    async def show_all(self):
        return await self.task_service.show_all()

    async def update_task(self, task_id: int, data: Union[TaskUpdateStatus, PatchTask]):
        result = await self.task_service.update_task(task_id, data)
        await self.task_service.update_redis("tasks:all")
        return result

    async def update_my_task(
        self, task_id: int, data: Union[TaskUpdateStatus, PatchTask], current_user: dict
    ):
        token_id = current_user.get("user_id")
        res = await self.task_service.show_task(token_id, task_id)
        if res is None:
            raise HTTPException(
                status_code=404, detail=["This is not your task or it does not exist"]
            )
        await self.task_service.update_redis("tasks:all")
        return await self.task_service.update_task(task_id, data)

    async def show_my_tasks(self, current_user: dict):
        user_id = current_user.get("user_id")
        return await self.task_service.show_my_tasks(user_id)
