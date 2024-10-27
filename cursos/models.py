from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=50)
    comision = models.CharField(max_length=20)
    Profesor = models.CharField(max_length=50)
    Descripcion = models.TextField(max_length=200)
    cupo = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    imagen = models.ImageField(upload_to="producto/%Y/%m/%d", blank=True, null=True)
    direccion= models.CharField(max_length=200)

    def __str__(self):
        return "curso: " + self.nombre