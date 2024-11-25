from django.contrib import admin
from .models import Noticia

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion', 'contenido', 'imagen', 'mostrar', 'imagen_preview')
    list_filter = ('fecha_publicacion', 'mostrar')
    search_fields = ('titulo', 'contenido')
    ordering = ('-fecha_publicacion',)
    actions = ['marcar_como_visible', 'marcar_como_oculto']

    def imagen_preview(self, obj):
        """
        Devuelve una imagen de muestra de la imagen de la noticia.
        """
        if obj.imagen:
            return f'<img src="{obj.imagen.url}" width="100" />'
        return 'No Image'
    
    imagen_preview.allow_tags = True
    imagen_preview.short_description = 'Imagen'

    def save_model(self, request, obj, form, change):
        """
        Sobreescribe el método save_model para guardar la imagen en el servidor.
        """
        if not obj.mostrar:
            obj.fecha_publicacion = None
        super().save_model(request, obj, form, change)
    
    @admin.action(description='Marcar como visible')
    def marcar_como_visible(self, request, queryset):
        queryset.update(mostrar=True)

    @admin.action(description='Marcar como oculto')
    def marcar_como_oculto(self, request, queryset):
        queryset.update(mostrar=False)
        
admin.site.register(Noticia, NoticiaAdmin)