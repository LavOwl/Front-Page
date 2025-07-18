from database import db
from pymongo import DESCENDING

async def get_articles(skip: int = 0, limit: int = 10):
    query = db.articles.find().sort("date", DESCENDING).skip(skip).limit(limit)
    return await query.to_list(length=limit)