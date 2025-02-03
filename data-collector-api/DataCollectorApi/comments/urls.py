from django.urls import path
from .views import RedditCommentListView, RedditCommentDetailView

urlpatterns = [
    path('comments/', RedditCommentListView.as_view(), name='reddit-comment-list'),
    path('comments/<str:post_id>/', RedditCommentListView.as_view(), name='reddit-comment-list-by-post'),
    path('comments/<str:_id>/', RedditCommentDetailView.as_view(), name='reddit-comment-detail'),
]
