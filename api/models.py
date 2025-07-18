from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

class Article(BaseModel):
    id: str = Field(alias="_id")
    url: str
    title: str
    subtitle: Optional[str] = None
    author: List[str] = []
    date: datetime = datetime.now()
    body: str
    tags: List[str] = []
    newspaper: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed=True
