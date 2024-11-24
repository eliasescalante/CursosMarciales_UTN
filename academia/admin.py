from django.contrib import admin
from .models import Noticia

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

admin.site.register(Noticia, NoticiaAdmin)