from django.db import models
from django.conf import settings

class Noticia(models.Model):
    """
    Modelo para Noticia
    """
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='noticias/', null=True, blank=True)
    mostrar = models.BooleanField(default=True)

    def __str__(self):
        return f"esta clase es {self.titulo}"