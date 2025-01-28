from api.services.RedditService import RedditService

from celery import shared_task

@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def fetch_reddit_data(self):
        # service = RedditService()
        # service.fetch_and_save_posts(limit=100)
        print('Hello from cron task!')