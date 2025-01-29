import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DataCollectorApi.settings')
django.setup()

from api.services.RedditService import RedditService

service = RedditService()
service.fetch_and_save_birds_posts(limit=20)
service.fetch_and_save_aliens_posts(limit=20)
service.fetch_and_save_migration_posts(limit=20)
print("Posts and comments have been inserted into MongoDB!")
