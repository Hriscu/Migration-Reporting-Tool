from django.urls import path
from . import views

urlpatterns = [
    path('hello1/', views.hello1, name='hello1'),  # Ruta pentru pagina principală
    path('hello2/', views.hello2, name='hello2'),  # Ruta pentru pagina "About"
    path('hello3/', views.hello3, name='hello3'),  # Ruta pentru pagina "Contact"
]