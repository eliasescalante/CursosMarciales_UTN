from django.urls import path
from . import views

# Rutas de usuarios
urlpatterns = [
    path('home/', views.home_usuarios, name='home_usuarios'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('carrito/', views.mi_carrito, name='carrito'),
    path('carrito/eliminar-ticket/<int:ticket_id>/', views.eliminar_ticket_carrito, name='eliminar_ticket_carrito'),
]
