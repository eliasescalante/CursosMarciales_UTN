from django.contrib import admin
from .models import Sede, Clase, InscripcionClase, Noticia

class SedeAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'direccion']

class ClaseAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'profesor', 'sede', 'dia', 'horario']
    list_filter = ['sede', 'profesor', 'dia']
    search_fields = ['nombre', 'profesor']

class InscripcionClaseAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'clase', 'fecha_inscripcion']
    search_fields = ['usuario__username', 'clase__nombre']

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion', 'contenido', 'imagen', 'mostrar', 'imagen_preview')
    list_filter = ('fecha_publicacion', 'mostrar')  # Agregamos un filtro para 'mostrar'
    search_fields = ('titulo', 'contenido')
    ordering = ('-fecha_publicacion',)

    # Si deseas que la imagen se muestre correctamente en el panel de administración
    def imagen_preview(self, obj):
        if obj.imagen:
            return f'<img src="{obj.imagen.url}" width="100" />'
        return 'No Image'
    
    imagen_preview.allow_tags = True
    imagen_preview.short_description = 'Imagen'

    # Mostrar/ocultar la noticia
    def save_model(self, request, obj, form, change):
        if not obj.mostrar:  # Si la noticia no está marcada como visible, la ocultamos
            obj.fecha_publicacion = None  # Esto es opcional, dependiendo de cómo manejes las fechas
        super().save_model(request, obj, form, change)

admin.site.register(Sede, SedeAdmin)
admin.site.register(Clase, ClaseAdmin)
admin.site.register(InscripcionClase, InscripcionClaseAdmin)
admin.site.register(Noticia, NoticiaAdmin)