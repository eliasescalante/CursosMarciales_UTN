from .models import Curso, Ticket
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def home_cursos(request):
    cursos = Curso.objects.all()  # O la consulta que necesites

    # Filtrar por nombre si se especifica
    query = request.GET.get('q', '')
    if query:
        cursos = cursos.filter(nombre__icontains=query)
    
    # Ordenar por precio o por nombre
    order = request.GET.get('order', '')
    if order == 'alfabetico':
        cursos = cursos.order_by('nombre')
    elif order == 'precio':
        cursos = cursos.order_by('precio')

    return render(request, 'cursos/home.html', {'cursos': cursos})

def noticias(request):
    return render(request, 'cursos/noticias.html')

# Vista para la página de mis cursos
# def mis_cursos(request):
#    return render(request, 'cursos/mis_cursos.html')


@login_required
def inscribirse_curso(request, curso_id):
    """
    Vista para inscribirse en un curso
    """
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
    ticket= Ticket.objects.create(usuario=usuario, curso=curso, estado='pendiente')
    curso.cupo -= 1
    curso.save()
    messages.success(request, f'Te has inscrito en el curso "{curso.nombre}" con éxito.  Tu ticket ID es: {ticket.id}')
    
    # Redirigir a mis cursos con la información del ticket
    return redirect('mis_cursos')

@login_required
def mis_cursos(request):
    """
    Vista para la página de mis cursos
    """
    tickets = Ticket.objects.filter(usuario=request.user).select_related('curso')
    cursos = [{'curso': ticket.curso, 'ticket_id': ticket.id} for ticket in tickets]
    print(cursos)

    return render(request, 'cursos/mis_cursos.html', {'cursos': cursos})


def detalle_curso(request, curso_id):
    """
    Vista para la página de detalles de un curso
    """
    curso = get_object_or_404(Curso, id=curso_id)
    usuario = request.user

    # Verificar si el usuario ya está inscrito en el curso
    inscripto = Ticket.objects.filter(usuario=usuario, curso=curso).exists()
    cupos = curso.cupo <= 0

    return render(request, 'cursos/detalle_curso.html', {'curso': curso, 'inscripto': inscripto, 'cupos': cupos})



@login_required
def desuscribirse_curso(request, ticket_id):
    """
    Vista para desuscribirse de un curso
    """
    try:
        ticket = Ticket.objects.get(id=ticket_id, usuario=request.user)
        ticket.delete()
        # Se devuelve una respuesta JSON con el mensaje y estado de éxito
        return JsonResponse({'success': True, 'message': f"Te has desuscripto del curso: {ticket.curso.nombre} con éxito."})
    except Ticket.DoesNotExist:
        # Si no se encuentra el ticket, se devuelve un mensaje de error
        return JsonResponse({'success': False, 'message': "No se pudo completar la desuscripción. El ticket no existe o no tienes permiso."})

