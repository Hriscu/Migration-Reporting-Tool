from datetime import datetime
import praw
from django.conf import settings
import spacy
from geopy.geocoders import Nominatim

from api.data.RedditComment import RedditComment
from api.data.DataPreprocessor import DataPreprocessor
from api.data.RedditCommentsRepository import RedditCommentsRepository
from api.data.RedditPostsRepository import RedditPostsRepository
from api.data.RedditPost import RedditPost


class RedditService:
    def __init__(self):
        self.repository = RedditPostsRepository()
        self.comments_repository = RedditCommentsRepository()
        self.preprocessor = DataPreprocessor()
        self.reddit = praw.Reddit(
            client_id=settings.REDDIT_CLIENT_ID,
            client_secret=settings.REDDIT_CLIENT_SECRET,
            user_agent=settings.REDDIT_USER_AGENT
        )
        self.nlp = spacy.load("en_core_web_sm")
        self.geolocator = Nominatim(user_agent="reddit_location_extractor")

    def extract_comments(self, comments):
        comment_strings = []
        for comment in comments:
            # Presupunem că cheia care conține textul comentariului este 'text'
            if 'text' in comment:  # Verificăm dacă există această cheie
                comment_strings.append(comment['text'])
        return comment_strings

    def get_comments_from_subreddit(self, subreddit_name):
        print(f"Fetching comments for subreddit: {subreddit_name}")
        posts = list(self.repository.find({"subreddit": subreddit_name}))
        comments = []
        for post in posts:
            post_comments = list(self.comments_repository.find({"post_id": post["_id"]}))
            comments.extend(post_comments)
        print(f"Fetched {len(comments)} comments.")
    
        # Extragem doar stringurile de comentarii
        comment_strings = self.extract_comments(comments)
        return comment_strings

    
    def extract_location(self, text):
        """Extrage locațiile geopolitice din text și coordonatele lor."""
        doc = self.nlp(text)
        locations = [ent.text for ent in doc.ents if ent.label_ == "GPE"]

        # Extragem o singură locație (dacă există mai multe, o preluăm doar pe prima)
        location = locations[0] if locations else None
        latitude = None
        longitude = None

        # Obține coordonatele locației dacă este disponibilă
        if location:
            try:
                geocode_result = self.geolocator.geocode(location)
                if geocode_result:
                    latitude = geocode_result.latitude
                    longitude = geocode_result.longitude
            except Exception as e:
                print(f"Error geocoding {location}: {e}")

        return {"location": location, "latitude": latitude, "longitude": longitude}

    def extract_keywords_from_subreddit(self, subreddit_name, text):
        """Extrage cuvinte cheie din familia lexicală a subreddit-ului."""
        if subreddit_name == "aliens":
            keywords = ["alien", "extraterrestrial", "ufo", "space", "contact", "life"]
        elif subreddit_name == "birds":
            keywords = ["bird", "birds", "migration", "feathers", "flight", "avian"]
        elif subreddit_name == "migration":
            keywords = ["migration", "refugees", "displacement", "border", "asylum", "human movement"]
        else:
            keywords = []
        return [word for word in keywords if word.lower() in text.lower()]

    def extract_media_urls(self, media):
        """Extrage URL-uri de media (video sau imagini)."""
        if media and isinstance(media, dict):
            return [media.get("reddit_video", {}).get("fallback_url")] if "reddit_video" in media else []
        return []

    def fetch_and_save_comments(self, post_id, subreddit_name):
        """Fetch and save comments for a given post."""
        post = self.reddit.submission(id=post_id)
        post.comments.replace_more(limit=10)
        count = 0

        for comment in post.comments.list():
            keywords = self.extract_keywords_from_subreddit(subreddit_name, comment.body)
            location_data = self.extract_location(comment.body)
            comment_data = {
                "comment_id": comment.id,
                "post_id": post_id,
                "text": self.preprocessor.preprocess_post(comment.body),
                "created_at": datetime.fromtimestamp(comment.created_utc),
                "score": comment.score,
                "is_submitter": comment.is_submitter,
                "keywords": keywords,
                "location": location_data["location"],
                "latitude": location_data["latitude"],
                "longitude": location_data["longitude"]
            }
            self.comments_repository.save(RedditComment.from_dict(comment_data))

            count += 1
            if count >= 50:
                break

    def fetch_and_save_posts(self, subreddit_name, limit=10):
        """Fetch and save posts from a given subreddit."""
        subreddit = self.reddit.subreddit(subreddit_name)
        for post in subreddit.hot(limit=limit):
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
                "media_urls": self.extract_media_urls(post.media),
                "keywords": self.extract_keywords_from_subreddit(post.subreddit.display_name, post.title + " " + (post.selftext or "")),
                "location": location_data["location"],
                "latitude": location_data["latitude"],
                "longitude": location_data["longitude"]
            }
            self.repository.save(RedditPost.from_dict(post_data))
            self.fetch_and_save_comments(post_data["post_id"], post_data["subreddit"])

    def fetch_and_save_birds_posts(self, limit=10):
        self.fetch_and_save_posts("birding", limit)

    def fetch_and_save_aliens_posts(self, limit=10):
        self.fetch_and_save_posts("aliens", limit)

    def fetch_and_save_migration_posts(self, limit=10):
        self.fetch_and_save_posts("migration", limit)
