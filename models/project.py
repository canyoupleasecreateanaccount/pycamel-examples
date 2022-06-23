from pydantic import BaseModel


class Support(BaseModel):
    url: str
    text: str


class Meta(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    support: Support
