import os  
import django
import asyncio
import asyncpraw
import spacy
from geopy.geocoders import Nominatim
from datetime import datetime
from django.conf import settings

from api.data.RedditComment import RedditComment
from api.data.RedditPost import RedditPost
from api.data.RedditCommentsRepository import RedditCommentsRepository
from api.data.RedditPostsRepository import RedditPostsRepository
from api.data.DataPreprocessor import DataPreprocessor

# Set Django configuration
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DataCollectorApi.settings')
django.setup()

class RedditStreamService:
    def __init__(self):
        self.repository = RedditPostsRepository()
        self.comments_repository = RedditCommentsRepository()
        self.preprocessor = DataPreprocessor()
        self.nlp = spacy.load("en_core_web_sm")
        self.geolocator = Nominatim(user_agent="reddit_location_extractor")
        # Initialize the Reddit client here, but don't create the session yet
        self.reddit = None

    def extract_location(self, text):
        doc = self.nlp(text)
        locations = [ent.text for ent in doc.ents if ent.label_ == "GPE"]
        location = locations[0] if locations else None
        latitude = longitude = None

        if location:
            try:
                geocode_result = self.geolocator.geocode(location)
                if geocode_result:
                    latitude, longitude = geocode_result.latitude, geocode_result.longitude
            except Exception as e:
                print(f"Error geocoding {location}: {e}")

        return {"location": location, "latitude": latitude, "longitude": longitude}

    async def process_post(self, post):
        location_data = self.extract_location(post.title + " " + (post.selftext or ""))

        post_data = {
            "post_id": post.id,
            "title": post.title,
            "text": self.preprocessor.preprocess_post(post.selftext) if post.is_self else None,
            "subreddit": post.subreddit.display_name,
            "created_at": datetime.fromtimestamp(post.created_utc),
            "score": post.score,
            "num_comments": post.num_comments,
            "is_self": post.is_self,
            "url": post.url,
            "location": location_data["location"],
            "latitude": location_data["latitude"],
            "longitude": location_data["longitude"]
        }

        self.repository.save(RedditPost.from_dict(post_data))
        print(f"✅ Saved post: {post.title}")

        await self.process_comments(post.id, post.subreddit.display_name)

    async def process_comments(self, post_id, subreddit_name):
        post = await self.reddit.submission(id=post_id)
        await post.comments.replace_more(limit=5)

        for comment in post.comments.list():
            location_data = self.extract_location(comment.body)

            comment_data = {
                "comment_id": comment.id,
                "post_id": post_id,
                "text": self.preprocessor.preprocess_post(comment.body),
                "created_at": datetime.fromtimestamp(comment.created_utc),
                "score": comment.score,
                "is_submitter": comment.is_submitter,
                "location": location_data["location"],
                "latitude": location_data["latitude"],
                "longitude": location_data["longitude"]
            }

            self.comments_repository.save(RedditComment.from_dict(comment_data))
            print(f"💬 Saved comment: {comment.body[:50]}...")

    async def stream_subreddit(self, subreddit_name):
        # Initialize the Reddit client within the task context
        self.reddit = asyncpraw.Reddit(
            client_id=settings.REDDIT_CLIENT_ID,
            client_secret=settings.REDDIT_CLIENT_SECRET,
            user_agent=settings.REDDIT_USER_AGENT
        )
        
        # Simply await subreddit instead of using async with
        subreddit = await self.reddit.subreddit(subreddit_name)
        print(f"🎧 Listening to {subreddit_name} in real-time...")

        async for post in subreddit.stream.submissions(skip_existing=True):
            await self.process_post(post)

    async def start_streaming(self):
        subreddits = ["aliens", "birding", "migration"]
        tasks = [self.stream_subreddit(sub) for sub in subreddits]

        await asyncio.gather(*tasks)

    async def close_reddit_session(self):
        if self.reddit:
            await self.reddit.close()  # Close the Reddit session properly

if __name__ == "__main__":
    service = RedditStreamService()
    try:
        asyncio.run(service.start_streaming())
    except Exception as e:
        print(f"Error during streaming: {e}")
    finally:
        # Ensure the session is closed after streaming ends
        asyncio.run(service.close_reddit_session())
