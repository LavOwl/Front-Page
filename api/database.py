from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "archive")

client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB]