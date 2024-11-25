from django.urls import path
from . import views

#Rutas de academia cursos
urlpatterns = [
    path('', views.index, name='index'),
    path('noticias/', views.noticias, name='noticias'),
]
