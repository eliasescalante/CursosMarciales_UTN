from django.contrib import admin
from .models import Consulta
from .models import Respuesta

class RespuestaInline(admin.TabularInline):
    """
    Inline para la respuesta de la consulta
    """
    model = Respuesta
    extra = 0

class Consultaadmin(admin.ModelAdmin):
    """
    Admin para la consulta
    """
    inlines = [RespuestaInline]
    list_display = ['nombre', 'descripcion','mail', 'estado_de_respuesta', 'telefono', 'fecha']
    list_filter = ['estado_respuesta', 'fecha']


admin.site.register(Consulta, Consultaadmin)