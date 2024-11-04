from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return HttpResponse("Página temporal")


def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Autenticación basada en el email en lugar de usuario
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige a la página principal o al dashboard
        else:
            messages.error(request, "Correo o contraseña incorrectos.")
    
    return render(request, 'usuarios/login.html')

def user_register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Ya existe un usuario con ese correo.")
        else:
            user = User.objects.create_user(username=email, email=email, password=password)
            login(request, user)  # Inicia sesión automáticamente tras el registro
            return redirect('home')  # Redirige a la página principal o al dashboard

    return render(request, 'usuarios/register.html')