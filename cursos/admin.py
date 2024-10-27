from django.contrib import admin
from .models import Curso  # Asegúrate de importar tu modelo

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
    ordering = ['-cupo']  # Puedes cambiar el orden según tus necesidades

# Registra el modelo y la clase de administración
admin.site.register(Curso, CursoAdmin)
