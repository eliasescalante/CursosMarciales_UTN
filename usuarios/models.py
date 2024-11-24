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

class Perfil(models.Model):
    user = models.OneToOneField(
        User,  # Relación con el modelo User personalizado
        on_delete=models.CASCADE,
        related_name='perfil'
    )
    bio = models.TextField(blank=True)  # Campo para una breve biografía
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación automática

    def __str__(self):
        return f"Perfil de {self.user.username}"