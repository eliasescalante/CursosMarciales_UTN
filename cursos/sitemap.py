from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from cursos.models import Curso

class CursoSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Curso.objects.all()

    def location(self, obj):
        return reverse('detalle_curso', args=[obj.id])

    def lastmod(self, obj):
        return None