from django.urls import path
from . import views

#Rutas de cursos
urlpatterns = [
    path('home/', views.home_cursos, name='home_cursos'),
    path('noticias/', views.noticias, name='noticias'),
    path('mis-cursos/', views.mis_cursos, name='mis_cursos'),
    path('inscribirse/<int:curso_id>/', views.inscribirse_curso, name='inscribirse_curso'),
    path('detalle/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
    path('desuscribirse/<int:ticket_id>/', views.desuscribirse_curso, name='desuscribirse_curso'),
]
