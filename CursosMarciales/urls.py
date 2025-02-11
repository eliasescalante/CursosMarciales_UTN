"""
URL configuration for CursosMarciales project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.shortcuts import redirect

#Rutas principales de la aplicacion
urlpatterns = [
    path("admin/", admin.site.urls),
    path("cursos/", include('cursos.urls')),
    path("usuarios/", include('usuarios.urls')),
    path("contacto/", include('contacto.urls')),
    path("api/v1.0/", include('cursosrestapi.urls')),
    path("captcha/", include('captcha.urls')),
    path("", include('academia.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
