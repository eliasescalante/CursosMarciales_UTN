from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Perfil
from django.utils.html import format_html

class CustomUserAdmin(UserAdmin):
    # Campos a mostrar en la lista del admin
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'ciudad', 'preview_image')
    
    # Campos que se pueden buscar
    search_fields = ('username', 'email', 'first_name', 'last_name')
    
    # Filtros disponibles en la barra lateral
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'ciudad')

    # Configuración de los grupos de campos en el formulario de edición
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'last_name', 'email', 'fecha_nacimiento', 'imagen', 'ciudad', 'domicilio', 'telefono')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas Importantes', {'fields': ('last_login', 'date_joined')}),
    )

    # Campos a mostrar en el formulario de creación
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'ciudad', 'imagen'),
        }),
    )

    # Ordenar por defecto por username
    ordering = ('username',)

    def preview_image(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="50" style="border-radius:50%;">', obj.imagen.url)
        return "Sin imagen"

    preview_image.short_description = "Imagen de Perfil"


# Personalizar el admin para el modelo Perfil
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'fecha_creacion')  # Campos visibles en la lista
    search_fields = ('user__username', 'user__email', 'bio')  # Campos buscables
    list_filter = ('fecha_creacion',)  # Filtros en la barra lateral
    ordering = ('-fecha_creacion',)  # Ordenar por fecha de creación descendente
    readonly_fields = ('fecha_creacion',)  # Evitar que se edite la fecha de creación

    def has_add_permission(self, request):
        """Evitar que se añadan perfiles desde el admin, ya que se crean automáticamente."""
        return False
