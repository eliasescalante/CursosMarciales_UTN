from django.contrib import admin
from .models import Curso , Ticket

class CursoAdmin(admin.ModelAdmin):
    # Puedes definir qué campos se mostrarán en el formulario de creación/edición
    fieldsets = [
        ("Información del Curso", {"fields": ["nombre", "comision", "Profesor", "Descripcion", "cupo", "precio", "imagen", "direccion"]}),
    ]
    
    # Campos que se mostrarán en la lista de cursos en la vista admin
    list_display = ['nombre', 'comision', 'Profesor', 'precio', 'cupo']
    
    # Permitir filtrado y búsqueda
    list_filter = ('comision', 'Profesor')
    search_fields = ('nombre', 'Profesor')
    ordering = ['-cupo']

class TicketAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'curso', 'fecha_compra', 'estado']
    list_filter = ['estado']
    search_fields = ['usuario__username', 'curso__nombre']

# Registra el modelo y la clase de administración
admin.site.register(Curso, CursoAdmin)
admin.site.register(Ticket, TicketAdmin)
