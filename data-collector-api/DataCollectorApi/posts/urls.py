from django.urls import path
from .views import RedditPostListView, RedditPostDetailView

urlpatterns = [
    path('posts/', RedditPostListView.as_view(), name='reddit-post-list'),
    path('posts/<str:_id>/', RedditPostDetailView.as_view(), name='reddit-post-detail'),
]
