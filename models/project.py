from pydantic import BaseModel


class Meta(BaseModel):
    total: int
    limit: int
    offset: int
