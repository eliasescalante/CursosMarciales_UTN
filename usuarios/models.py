from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario              = models.CharField(max_length=150, blank=False, null=True)
    imagen               = models.ImageField(upload_to="producto/%Y/%m/%d", default='defecto/defecto.png', blank=True, null=True)
    nombre               = models.CharField(max_length=50)
    apellido             = models.CharField(max_length=50)
    email                = models.EmailField(max_length=100, blank=False, null=True)
    fecha_nacimiento     = models.DateField(blank=True, null=True)
    pais                 = models.CharField(max_length=30, blank=True)
    provincia            = models.CharField(max_length=40, blank=True)
    ciudad               = models.CharField(max_length=40, blank=True)
    domicilio            = models.CharField(max_length=80, blank=True)
    codigo_postal        = models.CharField(max_length=50, blank=True)
    telefono             = models.CharField(max_length=30, blank=True)
    celular              = models.CharField(max_length=30, blank=True)
    documento            = models.CharField(max_length=30, blank=True)
    cuit                 = models.CharField(max_length=30, blank=True)
    Graduacion           = models.CharField(max_length=200)

    def __str__(self):
        return f"usuario: {self.usuario}"