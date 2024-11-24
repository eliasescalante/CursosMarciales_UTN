from .models import Curso, Ticket
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

def home_cursos(request):
    cursos = Curso.objects.all()  # O la consulta que necesites
    return render(request, 'home.html', {'cursos': cursos})

def noticias(request):
    return render(request, 'cursos/noticias.html')

# Vista para la página de mis cursos
"""
def mis_cursos(request):
    return render(request, 'cursos/mis_cursos.html')
"""

@login_required
def inscribirse_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    usuario = request.user

    # Verificar si ya está inscrito
    if Ticket.objects.filter(usuario=usuario, curso=curso).exists():
        messages.warning(request, f'Ya estás inscrito en el curso "{curso.nombre}".')
        return redirect('detalle_curso', curso_id=curso.id)

    # Verificar si hay cupo
    if curso.cupo <= 0:
        messages.error(request, f'El curso "{curso.nombre}" no tiene cupos disponibles.')
        return redirect('detalle_curso', curso_id=curso.id)

    # Crear el ticket y reducir el cupo
    Ticket.objects.create(usuario=usuario, curso=curso, estado='pendiente')
    curso.cupo -= 1
    curso.save()
    messages.success(request, f'Te has inscrito en el curso "{curso.nombre}" con éxito.')
    return redirect('mis_cursos')

@login_required
def mis_cursos(request):
    # Recuperar todos los tickets del usuario logueado
    tickets = Ticket.objects.filter(usuario=request.user).select_related('curso')

    # Extraer los cursos de los tickets
    # Crear una lista de diccionarios con la información necesaria para la vista
    cursos = [{'curso': ticket.curso, 'ticket_id': ticket.id} for ticket in tickets]
    # Depurar el contexto
    print(cursos)  # Verifica los datos en consola

    return render(request, 'cursos/mis_cursos.html', {'cursos': cursos})

def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    return render(request, 'cursos/detalle_curso.html', {'curso': curso})

@login_required
def desuscribirse_curso(request, ticket_id):
    try:
        # Buscar el ticket correspondiente
        ticket = Ticket.objects.get(id=ticket_id, usuario=request.user)
        ticket.delete()
        # Mensaje de éxito
        messages.success(request, f"Te has desuscripto del curso: {ticket.curso.nombre} con éxito.")
    except Ticket.DoesNotExist:
        # Mensaje de error
        messages.error(request, "No se pudo completar la desuscripción. El ticket no existe o no tienes permiso.")
    return redirect('mis_cursos')