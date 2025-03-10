from .models import Curso, Ticket
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings
import mercadopago

def home_cursos(request):
    """
    View para a página inicial
    """
    cursos = Curso.objects.all()

    query = request.GET.get('q', '')
    if query:
        cursos = cursos.filter(nombre__icontains=query)
    
    order = request.GET.get('order', '')
    if order == 'alfabetico':
        cursos = cursos.order_by('nombre')
    elif order == 'precio':
        cursos = cursos.order_by('precio')

    return render(request, 'cursos/home.html', {'cursos': cursos})

def noticias(request):
    """
    View para a página de notícias.
    """
    return render(request, 'cursos/noticias.html')


@login_required
def inscribirse_curso(request, curso_id):
    """
    Vista para inscribirse en un curso
    """
    curso = get_object_or_404(Curso, id=curso_id)
    usuario = request.user

    # Verifica si el usuario ya está inscrito en el curso
    if Ticket.objects.filter(usuario=usuario, curso=curso).exists():
        messages.warning(request, f'Ya estás inscrito en el curso "{curso.nombre}".')
        return redirect('detalle_curso', curso_id=curso.id)

    # Verifica si el curso tiene cupos disponibles
    if curso.cupo <= 0:
        messages.error(request, f'El curso "{curso.nombre}" no tiene cupos disponibles.')
        return redirect('detalle_curso', curso_id=curso.id)

    # Crea el ticket y actualiza el cupo del curso
    ticket = Ticket.objects.create(usuario=usuario, curso=curso, estado='pendiente')
    curso.cupo -= 1
    curso.save()

    # Mensaje de éxito
    messages.success(request, f'Te has inscrito en el curso "{curso.nombre}" con éxito. Tu ticket ID es: {ticket.id}')
    
    # Redirige a la vista de detalles del ticket
    return redirect('ticket', ticket_id=ticket.id)


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
        return JsonResponse({'success': True, 'message': f"Te has desuscripto del curso: {ticket.curso.nombre} con éxito."})
    except Ticket.DoesNotExist:
        return JsonResponse({'success': False, 'message': "No se pudo completar la desuscripción. El ticket no existe o no tienes permiso."})

@login_required
def ticket_detalle(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, usuario=request.user)

    # Configurar SDK de Mercado Pago
    sdk = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_TOKEN)

    # Crear preferencia de pago
    preference_data = {
        "items": [
            {
                "title": ticket.curso.nombre,
                "quantity": 1,
                "currency_id": "ARS",
                "unit_price": float(ticket.curso.precio)
            }
        ],
        "payer": {
            "email": request.user.email
        },
        "back_urls": {
            "success": request.build_absolute_uri('/usuarios/carrito/'),
            "failure": request.build_absolute_uri('/usuarios/carrito/'),
            "pending": request.build_absolute_uri('/usuarios/carrito/')
        },
        "auto_return": "approved"
    }

    preference_response = sdk.preference().create(preference_data)

    if "response" in preference_response and "id" in preference_response["response"]:
        payment_url = preference_response["response"].get("init_point")
    else:
        # Si Mercado Pago no devuelve un 'id', mostramos un error en la consola
        print("Error al crear la preferencia de Mercado Pago:", preference_response)
        preference_id = None

    return render(request, 'cursos/ticket.html', {'ticket': ticket, 'payment_url': payment_url})


def confirmar_pago(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    # Si el pago es correcto, actualizamos el curso y el carrito
    usuario = request.user
    if Carrito.objects.filter(usuario=usuario, curso=curso).exists():
        carrito = Carrito.objects.get(usuario=usuario, curso=curso)
        carrito.delete()  # Borra el curso del carrito

        # Cambia el estado del curso a "pagado"
        usuario_curso = UsuarioCurso.objects.get(usuario=usuario, curso=curso)
        usuario_curso.estado = "pagado"
        usuario_curso.save()

        # Agregar un mensaje de éxito
        messages.success(request, f"Gracias por tu compra. El curso '{curso.nombre}' ha sido aprobado.")

    return redirect('mis_cursos')