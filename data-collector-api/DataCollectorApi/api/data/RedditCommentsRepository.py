# RedditCommentsRepository.py
from api.data import RedditComment
from api.data.MongoDbClient import MongoDbClient

class RedditCommentsRepository:
    def __init__(self, mongo_uri=None, mongo_db_name=None):
        self.db = MongoDbClient(mongo_uri, mongo_db_name).get_db()
        self.collection = self.db['reddit_comments']

    def get_all(self):
        comments = self.collection.find()
        return comments

    def get_by_post_id(self, post_id):
        return self.collection.find({"post_id": post_id})

    def save(self, comment: RedditComment):
        self.collection.update_one({"_id": comment.id}, {"$set": comment.__dict__()}, upsert=True)

    def find(self, query):
        return list(self.collection.find(query))
