from database import db
from pymongo import DESCENDING
from bson import ObjectId
from fastapi import HTTPException

async def get_articles(skip: int = 0, limit: int = 10):
    query = db.articles.find().sort("date", DESCENDING).skip(skip).limit(limit)
    articles = await query.to_list(length=limit)
    for article in articles:
        article["_id"] = str(article["_id"])
    return articles

async def get_article_by_id(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID format")
    document = await db.articles.find_one({"_id": ObjectId(id)})
    if not document:
        raise HTTPException(status_code=404, detail="Article not found")
    document["_id"] = str(document["_id"])
    return document