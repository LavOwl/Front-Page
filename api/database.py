from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
import os

from typing import Any

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "archive")

client: AsyncIOMotorClient[Any] = AsyncIOMotorClient(MONGO_URI)
db: AsyncIOMotorDatabase[Any] = client[MONGO_DB]