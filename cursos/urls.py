from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_cursos, name='home_cursos'),  # Asegúrate de que sea 'home' en lugar de 'index'
]
