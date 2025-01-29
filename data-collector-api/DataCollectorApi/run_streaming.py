import os
import django
import asyncio
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DataCollectorApi.settings')
django.setup()

from api.services.RedditStreamService import RedditStreamService

service = RedditStreamService()

if __name__ == "__main__":
    asyncio.run(service.start_streaming())
