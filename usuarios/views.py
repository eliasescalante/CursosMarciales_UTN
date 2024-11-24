from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, PerfilUpdateForm
from .models import User
from cursos.models import Curso
from django.contrib.auth.decorators import login_required
from django.contrib.messages import get_messages

# Vista para el inicio
@login_required
def home_usuarios(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/home.html', {'cursos': cursos})  # Muestra la página de inicio solo para usuarios logueados
    
# Vista para el login de usuario
def user_login(request):

    storage = get_messages(request)
    for _ in storage:  # Esto vacía los mensajes existentes
        pass

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Verifica si el email existe en el modelo Datosusuario
            usuario = User.objects.get(email=email)
            # Verifica si la contraseña es correcta
            if usuario.check_password(password):
                login(request, usuario)  # Inicia sesión con el modelo User de Django
                return redirect('home_usuarios')  # Redirige a la página de inicio
            else:
                messages.error(request, "Correo o contraseña incorrectos.")
        except User.DoesNotExist:
            messages.error(request, "El usuario no se encuentra regsitrado.")
    
    return render(request, 'usuarios/login.html')

def user_logout(request):
    logout(request)
    return redirect('index')

# Vista para el registro de usuario
def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)  # Asegúrate de pasar request.FILES aquí
        if form.is_valid():
            user = form.save(commit=False)  # No guardar aún para poder encriptar la contraseña
            user.set_password(request.POST['password'])  # Encriptar la contraseña
            user.save()  # Guardar el usuario en la base de datos
            messages.success(request, "Te has registrado con éxito.")  # Mensaje de éxito
            return redirect('login')  # Redirigir al login después de registrar el usuario
    else:
        form = UserRegistrationForm()
    return render(request, 'usuarios/register.html', {'form': form})

@login_required
def perfil(request):
    # Obtener el usuario logueado
    user = request.user
    perfil = user.perfil

    if request.method == 'POST':
        # Crear los formularios con los datos recibidos del POST
        user_form = UserUpdateForm(request.POST, request.FILES, instance=user)
        perfil_form = PerfilUpdateForm(request.POST, instance=perfil)

        if user_form.is_valid() and perfil_form.is_valid():
            # Guardar los formularios si son válidos
            user_form.save()
            perfil_form.save()
            messages.success(request, 'Tu perfil ha sido actualizado correctamente.')
            return redirect('perfil')  # Redirigir a la misma página

    else:
        # Si es GET, llenar los formularios con los datos actuales
        user_form = UserUpdateForm(instance=user)
        perfil_form = PerfilUpdateForm(instance=perfil)

    return render(request, 'usuarios/perfil.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    })

def mi_carrito(request):
    return render(request, 'usuarios/carrito.html')