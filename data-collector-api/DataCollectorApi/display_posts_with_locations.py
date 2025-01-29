import os
import django
from dotenv import load_dotenv  # Pentru a încărca variabilele din .env

# Încarcă variabilele din fișierul .env
load_dotenv()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DataCollectorApi.settings')
django.setup()
# Inițializează Django
django.setup()

# Importuri proiect
from api.data.RedditPostsRepository import RedditPostsRepository
from api.data.RedditCommentsRepository import RedditCommentsRepository

def display_posts_with_locations():
    posts_repository = RedditPostsRepository()
    comments_repository = RedditCommentsRepository()

    posts = posts_repository.find({"location": {"$ne": None}})
    for post in sorted(posts, key=lambda x: x.get("subreddit", "").lower()):
        print(f"{post['subreddit']} - {post['title']} - {post['location']} ({post['latitude']}, {post['longitude']}):")
        comments = comments_repository.find({"post_id": post["_id"]})
        for comment in comments:
            print(f"    {comment['text']}")

if __name__ == "__main__":
    display_posts_with_locations()
