import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DataCollectorApi.settings')
django.setup()

from api.services.RedditService import RedditService

service = RedditService()
service.fetch_and_save_posts(limit=5)
print("Posts and comments have been inserted into MongoDB!")
