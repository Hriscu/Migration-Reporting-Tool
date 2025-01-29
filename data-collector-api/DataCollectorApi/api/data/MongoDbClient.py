# MongoDbClient.py
from pymongo import MongoClient
import os

class MongoDbClient:
    def __init__(self, mongo_uri=None, mongo_db_name=None):
        self.mongo_uri = mongo_uri or os.getenv("MONGO_URI")
        self.mongo_db_name = mongo_db_name or os.getenv("MONGO_DB_NAME")
        
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db_name]

    def get_db(self):
        return self.db
