from django.urls import path
from . import views

urlpatterns = [
    # path('json/bird/', views.get_bird_info_json, name="bird-info-json"),
    path('posts-view/', views.get_posts_view, name="posts-view"),
    path('comments-view/', views.get_comments_view, name="comments-view"),
    path('birds-view/', views.get_birds_view, name="birds-view"),
    path('locations-view/', views.get_locations_view, name="locations-view"),
    # path('make-relations/', views.make_relations, name="make-relations"),
    path('sent-relations-to-fuseki/', views.get_and_insert_location_data, name="sent-relations-to-fuseki"),
]