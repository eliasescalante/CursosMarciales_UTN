from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator  # Asegúrate de importar esto

from django.db import models

class User(AbstractUser):
    # Campos adicionales
    imagen = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    ciudad = models.CharField(max_length=40, blank=True)
    domicilio = models.CharField(max_length=80, blank=True)
    telefono = models.CharField(max_length=30, blank=True)

    # Agregar un campo de correo electrónico
    email = models.EmailField(unique=True, validators=[EmailValidator()])

    def __str__(self):
        return "usuario: " + self.username
