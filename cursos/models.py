from django.db import models
from django.conf import settings

# Create your models here.
class Curso(models.Model):
    """
    Modelo para representar un curso.
    """

    nombre = models.CharField(max_length=50)
    comision = models.CharField(max_length=20)
    Profesor = models.CharField(max_length=50)
    Descripcion = models.TextField(max_length=500)
    cupo = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    imagen = models.ImageField(upload_to="producto/%Y/%m/%d", blank=True, null=True)
    direccion= models.CharField(max_length=200)

    def __str__(self):
        return "curso: " + self.nombre

class Ticket(models.Model):
    """
    Modelo para representar un ticket.
    """
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('pagado', 'Pagado')], default='pendiente')

    def __str__(self):
        return f"Ticket para {self.usuario.username} - Curso: {self.curso.nombre} - Estado: {self.estado}"