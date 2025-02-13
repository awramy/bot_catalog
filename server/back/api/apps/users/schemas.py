from pydantic import BaseModel
from enum import Enum


class RoleEnum(str, Enum):
    USER = "USER"
    ADMIN = "ADMIN"


class UserBase(BaseModel):
    id: int
    name: str
    role: RoleEnum
    balance: float


class UserCreate(UserBase):
    pass


class User(UserBase):
    class Config:
        orm_mode = True
