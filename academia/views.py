from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .models import Noticia

def index(request):
    return render(request, 'academia/index.html', {'MEDIA_URL' : settings.MEDIA_URL})

def noticias(request):
    noticias = Noticia.objects.all().order_by('-fecha_publicacion')
    return render(request, 'academia/noticias.html', {'noticias': noticias})