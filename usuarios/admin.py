from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import User, Perfil

class CustomUserAdmin(UserAdmin):
    """
    Admin para el modelo usuario
    """

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'ciudad', 'preview_image')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'ciudad')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {
            'fields': ('first_name', 'last_name', 'email', 'fecha_nacimiento', 'imagen', 'ciudad', 'domicilio', 'telefono')
        }),
        ('Permisos', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Fechas Importantes', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'fecha_nacimiento', 'imagen', 'ciudad', 'domicilio', 'telefono')
        }),
    )

    ordering = ('username',)

    def preview_image(self, obj):
        """
        Mostrar una vista previa de la imagen de perfil en la lista de usuarios.
        """
        if obj.imagen:
            return format_html('<img src="{}" width="50" style="border-radius:50%;">', obj.imagen.url)
        return "Sin imagen"

    preview_image.short_description = "Imagen de Perfil"

admin.site.register(User, CustomUserAdmin)


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    """
    Admin para el modelo Perfil
    """
    list_display = ('user', 'bio', 'fecha_creacion')
    search_fields = ('user__username', 'user__email', 'bio')
    list_filter = ('fecha_creacion',)
    ordering = ('-fecha_creacion',)
    readonly_fields = ('fecha_creacion',) 

    def has_add_permission(self, request):
        """
        Para evitar que se agreguen perfiles desde el admin.
        """
        return False
