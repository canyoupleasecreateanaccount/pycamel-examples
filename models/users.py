from typing import List
from pydantic import BaseModel
from datetime import datetime
from models.project import Meta


class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class UserList(Meta):
    data: List[User]


class BaseUser(BaseModel):
    name: str
    job: str


class UserCreate(BaseUser):
    id: int
    createdAt: datetime

class UserUpdate(BaseUser):
    updatedAt: datetime

