from django.urls import path
from .controllers.reddit_controller import StartTask, StopTask

urlpatterns = [
    path("fetch-posts/start", StartTask.as_view(), name="collect_reddit_posts"),
    path("fetch-posts/stop", StopTask.as_view(), name="stop_collect_reddit_posts"),
]
