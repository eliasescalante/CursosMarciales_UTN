from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_usuarios, name='home_usuarios'),  # URL para home
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('perfil/', views.perfil, name='perfil')
]
