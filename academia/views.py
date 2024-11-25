from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from .models import Noticia

def index(request):
    return render(request, 'academia/index.html', {'MEDIA_URL' : settings.MEDIA_URL})

def noticias(request):
    """
    View que lista todas as notícias
    """
    noticias = Noticia.objects.all().order_by('-fecha_publicacion')
    return render(request, 'academia/noticias.html', {'noticias': noticias})

def detalle_noticia(request, noticia_id):
    """
    Vista para mostrar el detalle de una noticia
    """
    noticia = get_object_or_404(Noticia, id=noticia_id)
    return render(request, 'academia/detalle_noticia.html', {'noticia': noticia})