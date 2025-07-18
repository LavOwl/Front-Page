import pymongo
import os

class MongoPipeline:

    client = None
    db = None

    def open_spider(self, spider):
        mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
        mongo_db = os.getenv("MONGO_DB", "archive")
        self.client = pymongo.MongoClient(mongo_uri)
        self.db = self.client[mongo_db]

        self.db["articles"].create_index("url", unique=True)

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        collection = self.db["articles"]
        collection.update_one({"url": item["url"]}, {"$set": dict(item)}, upsert=True)
        return item