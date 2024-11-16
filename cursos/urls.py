from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Asegúrate de que sea 'home' en lugar de 'index'
]
