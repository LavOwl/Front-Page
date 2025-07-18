from fastapi import APIRouter, Query
from typing import List
from models import Article
from crud import get_articles, get_article_by_id

router = APIRouter()

@router.get("/articles", response_model=List[Article])
async def list_articles(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=100)):
    return await get_articles(skip=skip, limit=limit)

@router.get("/articles/{id}", response_model=Article)
async def show_article(id: str):
    return (await get_article_by_id(id))