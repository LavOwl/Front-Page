from typing import List, TypedDict
from datetime import datetime

class ArticleDict(TypedDict):
    url: str
    title: str | None
    subtitle: str | None
    author: List[str]
    tags: List[str]
    date: datetime
    body: str
    newspaper: str