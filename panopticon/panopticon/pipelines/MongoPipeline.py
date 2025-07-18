import pymongo
import os
from scrapy import Spider
from pymongo.database import Database
from pymongo.mongo_client import MongoClient
from ..classes.article_dictionary import ArticleDict
from typing import Any

class MongoPipeline:

    client: MongoClient[Any]
    db: Database[Any]

    def open_spider(self, spider: Spider):
        mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
        mongo_db = os.getenv("MONGO_DB", "archive")
        self.client = pymongo.MongoClient(mongo_uri)
        self.db = self.client[mongo_db]

        self.db["articles"].create_index("url", unique=True)

    def close_spider(self, spider: Spider):
        self.client.close()

    def process_item(self, item:ArticleDict, spider: Spider):
        collection = self.db["articles"]
        collection.update_one({"url": item["url"]}, {"$set": dict(item)}, upsert=True)
        return item