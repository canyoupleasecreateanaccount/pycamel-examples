from typing import List

from pydantic import BaseModel
from pydantic.color import Color

from models.project import Meta


class Resource(BaseModel):
    id: int
    name: str
    year: int
    color: Color
    pantone_value: str


class ResourceList(Meta):
    data: List[Resource]
