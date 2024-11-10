from django.contrib import admin
from .models import Sede, Clase, InscripcionClase

class SedeAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'direccion']

class ClaseAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'profesor', 'sede', 'dia', 'horario']
    list_filter = ['sede', 'profesor', 'dia']
    search_fields = ['nombre', 'profesor']

class InscripcionClaseAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'clase', 'fecha_inscripcion']
    search_fields = ['usuario__username', 'clase__nombre']

admin.site.register(Sede, SedeAdmin)
admin.site.register(Clase, ClaseAdmin)
admin.site.register(InscripcionClase, InscripcionClaseAdmin)
