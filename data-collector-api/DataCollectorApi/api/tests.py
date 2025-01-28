from django.test import TestCase

# Create your tests here.

from .services.reddit_service import RedditService
from .db.mongodb_client import db


class RedditServiceTestCase(TestCase):
    def setUp(self):
        self.service = RedditService()

    def test_fetch_posts(self):
        posts = self.service.fetch_posts_and_store(limit=2)
        self.assertIsInstance(posts, list)
        self.assertGreater(len(posts), 0)
        for post in posts:
            self.assertIn("post_id", post)
            self.assertIn("title1", post)
            was_post_inserted = db.posts.find_one({"post_id": post["post_id"]})
            self.assertIsNotNone(was_post_inserted)
