# views.py
import os
from dotenv import load_dotenv
from django.shortcuts import render
from api.data.RedditPostsRepository import RedditPostsRepository
from api.data.RedditCommentsRepository import RedditCommentsRepository

load_dotenv()

def display_posts_with_locations(request):
    mongo_uri = os.getenv("MONGO_URI")
    mongo_db_name = os.getenv("MONGO_DB_NAME")
    
    posts_repository = RedditPostsRepository(mongo_uri, mongo_db_name)
    comments_repository = RedditCommentsRepository(mongo_uri, mongo_db_name)

    posts = posts_repository.find({"location": {"$ne": None}})

    posts_data = []
    for post in sorted(posts, key=lambda x: x.get("subreddit", "").lower()):
        comments = comments_repository.find({"post_id": post["_id"]})
        post_info = {
            "subreddit": post["subreddit"],
            "title": post["title"],
            "location": post["location"],
            "latitude": post["latitude"],
            "longitude": post["longitude"],
            "comments": comments
        }
        posts_data.append(post_info)
    return render(request, "posts_with_locations.html", {"posts": posts_data})
