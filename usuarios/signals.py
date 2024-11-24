# usuarios/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Perfil

@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
        print("Se han creado un perfil para el usuario")