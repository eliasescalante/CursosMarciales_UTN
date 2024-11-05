from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),  # URL para home
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register')
]
