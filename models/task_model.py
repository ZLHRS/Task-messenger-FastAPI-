from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Enum as PgEnum
from database.db import Base
from enum import Enum


class TaskStatus(str, Enum):
    planned = "planned"
    active = "active"
    blocked = "blocked"
    finished = "finished"


class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(300), nullable=False)
    status: Mapped[TaskStatus] = mapped_column(
        PgEnum(TaskStatus), default=TaskStatus.planned, nullable=False
    )
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.users_id", ondelete="CASCADE")
    )
    user = relationship("User", back_populates="tasks")
