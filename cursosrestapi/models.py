from django.db import models

class CursosRestApi(models.Model):
    titulo=models.CharField(max_length=70)
    descripcion=models.TextField()