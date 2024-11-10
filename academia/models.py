from django.db import models
from django.conf import settings

class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return f"Sede: {self.nombre}"

class Clase(models.Model):
    nombre = models.CharField(max_length=50)
    profesor = models.CharField(max_length=50)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    dia = models.CharField(max_length=20)  # Ejemplo: 'Lunes'
    horario = models.TimeField()
    descripcion = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Clase: {self.nombre} ({self.dia} a las {self.horario})"

class InscripcionClase(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Usamos settings.AUTH_USER_MODEL
    clase = models.ForeignKey('Clase', on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} inscrito en {self.clase.nombre}"
