from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.get_reddit_posts, name="reddit-posts"),
    path('comments/', views.get_reddit_comments_json, name="reddit-comments"),
    path('insert-posts/', views.get_and_insert_posts, name="insert-posts"),
    path('insert-comments/', views.get_and_insert_comments, name="insert-comments"),
]