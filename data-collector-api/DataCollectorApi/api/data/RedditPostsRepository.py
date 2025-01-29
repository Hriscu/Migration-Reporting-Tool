# RedditPostsRepository.py
from api.data.MongoDbClient import MongoDbClient
from api.data.RedditPost import RedditPost

class RedditPostsRepository:
    def __init__(self, mongo_uri=None, mongo_db_name=None):
        self.db = MongoDbClient(mongo_uri, mongo_db_name).get_db()
        self.collection = self.db['reddit_posts']

    def get_all(self):
        posts = self.collection.find()
        return [RedditPost.from_dict(post) for post in posts]

    def save(self, post: RedditPost):
        self.collection.update_one({"_id": post.id}, {"$set": post.__dict__()}, upsert=True)

    def find(self, query):
        return list(self.collection.find(query))
