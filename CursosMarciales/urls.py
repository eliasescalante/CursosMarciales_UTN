from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.shortcuts import redirect
from academia.sitemap import AcademiaViewSitemap
from cursos.sitemap import CursoSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'noticias':AcademiaViewSitemap,
    'producto': CursoSitemap,
}

#Rutas principales de la aplicacion
urlpatterns = [
    path("admin/", admin.site.urls),
    path("cursos/", include('cursos.urls')),
    path("usuarios/", include('usuarios.urls')),
    path("contacto/", include('contacto.urls')),
    path("api/v1.0/", include('cursosrestapi.urls')),
    path("captcha/", include('captcha.urls')),
    path("", include('academia.urls')),
    path('sitemap.xml', sitemap, {'sitemaps' : sitemaps}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
