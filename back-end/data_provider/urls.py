from django.urls import path
from . import views

urlpatterns = [
    path('get-relations-for-posts/', views.get_relations_for_posts, name="get-relations-for-posts"),
    path('get-relations-for-comments/', views.get_relations_for_comments, name="get-relations-for-comments"),
    path('make-object-for-front/', views.make_object_for_front, name="make-object-for-front"),
]