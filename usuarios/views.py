from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, PerfilUpdateForm
from .models import User
from cursos.models import Curso
from django.contrib.auth.decorators import login_required
from django.contrib.messages import get_messages


@login_required
def home_usuarios(request):
    """
    Vista para el inicio de la aplicación.
    """
    cursos = Curso.objects.all()
    return render(request, 'cursos/home.html', {'cursos': cursos})

def user_login(request):
    """
    Vista para el login de usuario
    """
    storage = get_messages(request)
    for _ in storage:
        pass

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            usuario = User.objects.get(email=email)
            if usuario.check_password(password):
                login(request, usuario)
                return redirect('home_usuarios')
            else:
                messages.error(request, "Correo o contraseña incorrectos.")
        except User.DoesNotExist:
            messages.error(request, "El usuario no se encuentra regsitrado.")
    
    return render(request, 'usuarios/login.html')

def user_logout(request):
    """
    Vista para el logout de usuario
    """
    logout(request)
    return redirect('index')

def user_register(request):
    """
    Vista para el registro de usuario.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(request.POST['password'])
            user.save()
            messages.success(request, "Te has registrado con éxito.")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'usuarios/register.html', {'form': form})

@login_required
def perfil(request):
    """
    Vista para el perfil del usuario
    """
    user = request.user
    perfil = user.perfil
    return render(request, 'usuarios/perfil.html', {
        'user': user,
        'perfil': perfil
    })

@login_required
def editar_perfil(request):
    """
    Vista para editar el perfil de un usuario.
    """
    user = request.user
    perfil = user.perfil

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, request.FILES, instance=user)
        perfil_form = PerfilUpdateForm(request.POST, instance=perfil)

        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            messages.success(request, 'Tu perfil ha sido actualizado correctamente.')
            return redirect('perfil')

    else:
        user_form = UserUpdateForm(instance=user)
        perfil_form = PerfilUpdateForm(instance=perfil)

    return render(request, 'usuarios/editar_perfil.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    })

def mi_carrito(request):
    """
    Vista para mostrar el carrito de compras del usuario.
    """
    return render(request, 'usuarios/carrito.html')