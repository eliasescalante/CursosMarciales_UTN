from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Perfil

@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    """
    Crea un perfil para cada usuario creado.
    """
    if created:
        Perfil.objects.create(user=instance)
        print("Se han creado un perfil para el usuario")

@receiver(post_save, sender=Perfil)
def perfil_actualizado(sender, instance, created, **kwargs):
    """
    Cuando se actualiza un perfil, se actualiza el usuario asociado
    """
    if not created:
        print(f"El perfil de {instance.user.username} ha sido actualizado.")