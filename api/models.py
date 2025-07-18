from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class Article(BaseModel):
    url: str
    title: str
    subtitle: Optional[str] = None
    author: List[str] = []
    date: datetime = datetime.now()
    body: str
    tags: List[str] = []
    newspaper: str
