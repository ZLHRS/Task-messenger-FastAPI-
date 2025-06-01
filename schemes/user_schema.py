from pydantic import BaseModel, Field, ConfigDict, field_validator, EmailStr
from enum import Enum


class UserRole(str, Enum):
    admin = "admin"
    user = "user"


class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr = Field(..., min_length=12, max_length=60)
    password: str = Field(..., min_length=6, max_length=100)
    role: UserRole = UserRole.user

    @classmethod
    @field_validator("email")
    def check_gmail(cls, v):
        if not v.endswith("@gmail.com"):
            raise ValueError("Email must be a gmail.com address")
        return v


class CreateUser(UserBase):
    pass


class UserSchema(BaseModel):
    id: int
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr = Field(..., min_length=12, max_length=60)
    password: str = Field(..., min_length=6, max_length=100)
    role: UserRole = UserRole.user
    model_config = ConfigDict(from_attributes=True)

    @classmethod
    @field_validator("email")
    def check_gmail(cls, v):
        if not v.endswith("@gmail.com"):
            raise ValueError("Email must be a gmail.com address")
        return v


class UserUpdateRole(BaseModel):
    role: UserRole
    model_config = ConfigDict(from_attributes=True)
