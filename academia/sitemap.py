from django.contrib import sitemaps
from django.urls import reverse

class AcademiaViewSitemap(sitemaps.Sitemap):
    priority = 0.9
    changefreq = 'daily'

    def items(self):
        return ['noticias']
    def location(self, item):
        return reverse(item)