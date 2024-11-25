from django import forms
from django.contrib.auth.models import User
from .models import User, Perfil

class UserRegistrationForm(forms.ModelForm):
    """
    Formulario para el registro de usuario
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'fecha_nacimiento', 'ciudad', 'domicilio', 'telefono', 'imagen']
        widgets = {
            'password': forms.PasswordInput(),
        }

class UserUpdateForm(forms.ModelForm):
    """
    Formulario para actualizar los datos de un usuario.
    """
    imagen = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'imagen', 'fecha_nacimiento', 'ciudad', 'domicilio', 'telefono']

class PerfilUpdateForm(forms.ModelForm):
    """
    Formulario para actualizar los datos de un perfil.
    """
    class Meta:
        model = Perfil
        fields = ['bio']