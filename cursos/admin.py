from django.contrib import admin
from .models import Curso , Ticket

class CursoAdmin(admin.ModelAdmin):
    """
    Interfaz para el Admin de cursos
    """
    fieldsets = [
        ("Información del Curso", {"fields": ["nombre", "comision", "Profesor", "Descripcion", "cupo", "precio", "imagen", "direccion"]}),
    ]
    
    list_display = ['nombre', 'comision', 'Profesor', 'precio', 'cupo']
    
    list_filter = ('comision', 'Profesor')
    search_fields = ('nombre', 'Profesor')
    ordering = ['-cupo']

class TicketAdmin(admin.ModelAdmin):
    """
    Interfaz para el Admin de tickets
    """
    list_display = ['usuario', 'curso', 'fecha_compra', 'estado']
    list_filter = ['estado']
    search_fields = ['usuario__username', 'curso__nombre']

    def has_add_permission(self, request):
        """
        Para evitar que se agreguen perfiles desde el admin.
        """
        return False


admin.site.register(Curso, CursoAdmin)
admin.site.register(Ticket, TicketAdmin)
