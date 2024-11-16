from .models import Curso
from django.shortcuts import render

def home_cursos(request):
    cursos = Curso.objects.all()  # O la consulta que necesites
    return render(request, 'home.html', {'cursos': cursos})
