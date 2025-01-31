from django.urls import path
from . import views

urlpatterns = [
    path('json/', views.get_bird_info_json, name="bird-info-json"),
    path('rdf/', views.get_bird_info_rdf, name="bird-info-rdf"),
    path('insert-data/', views.get_and_insert_bird_data, name="insert-bird-data"),
]