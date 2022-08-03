from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: Optional[str]
    last_name: str
    company_id: Optional[int]


class User(UserBase):
    user_id: int
