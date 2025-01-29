from django.urls import path
from . import views
from .controllers.reddit_controller import StartTask, StopTask

urlpatterns = [
    path('posts_with_locations/', views.display_posts_with_locations, name='display_posts_with_locations'),
    path("fetch-posts/start", StartTask.as_view(), name="collect_reddit_posts"),
    path("fetch-posts/stop", StopTask.as_view(), name="stop_collect_reddit_posts"),
]
