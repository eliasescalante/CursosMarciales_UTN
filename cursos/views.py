from .models import Curso

def home(request):
    cursos = Curso.objects.all()  # O la consulta que necesites
    print(cursos)  # Verifica que los cursos están siendo recuperados correctamente
    return render(request, 'home.html', {'cursos': cursos})
