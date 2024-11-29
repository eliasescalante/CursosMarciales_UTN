from django.contrib import admin
from .models import Curso , Ticket
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render

class CursoAdmin(admin.ModelAdmin):
    """
    Interfaz para el Admin de cursos
    """
    fieldsets = [
        ("Información del Curso",
            {"fields":
                ["nombre", "comision", "Profesor",
                "Descripcion", "cupo", "precio",
                "imagen", "direccion"]}),
    ]

    list_display = ['nombre', 'comision', 'Profesor', 'precio', 'cupo']
    actions= ["export_a_json", "ver_cursos"]
    list_filter = ('comision', 'Profesor')
    search_fields = ('nombre', 'Profesor')
    ordering = ['-cupo']

    def export_a_json(self, request, queryset):
        """
        Exportar a JSON
        """
        response = HttpResponse(content_type="application/json")
        serializers.serialize("json", queryset, stream=response )
        return response

    def ver_cursos(self, request, queryset):
        """
        Ver cursos
        """
        cursos = queryset
        return render(request, "admin/cursos/cursos.html", {"cursos": cursos})

    ver_cursos.short_description = "Ver cursos seleccionados"

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
