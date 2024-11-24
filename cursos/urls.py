from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_cursos, name='home_cursos'),
    path('noticias/', views.noticias, name='noticias'),
    path('mis-cursos/', views.mis_cursos, name='mis_cursos'),
]
