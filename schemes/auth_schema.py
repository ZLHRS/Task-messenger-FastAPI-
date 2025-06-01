from pydantic import BaseModel


class LoginBase(BaseModel):
    username: str
    password: str
