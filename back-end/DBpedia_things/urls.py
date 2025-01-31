from django.urls import path
from . import views

urlpatterns = [
    path('json/bird/', views.get_bird_info_json, name="bird-info-json"),
    path('json/location/', views.get_location_info_json, name="location-info-json"),
    path('rdf/', views.get_bird_info_rdf, name="bird-info-rdf"),
    path('insert-bird-data/', views.get_and_insert_bird_data, name="insert-bird-data"),
    path('insert-location-data/', views.get_and_insert_location_data, name="insert-location-data"),
]