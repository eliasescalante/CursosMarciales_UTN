from .models import Curso
from django.shortcuts import render

def home_cursos(request):
    cursos = Curso.objects.all()  # O la consulta que necesites
    return render(request, 'home.html', {'cursos': cursos})

def noticias(request):
    return render(request, 'cursos/noticias.html')

# Vista para la página de mis cursos
def mis_cursos(request):
    return render(request, 'cursos/mis_cursos.html')