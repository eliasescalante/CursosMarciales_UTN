from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

def index(request):
    return render(request, 'academia/index.html', {'MEDIA_URL' : settings.MEDIA_URL})  # Asegúrate de que index.html esté en la carpeta correcta
