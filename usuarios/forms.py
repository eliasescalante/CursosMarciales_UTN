from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'fecha_nacimiento', 'ciudad', 'domicilio', 'telefono', 'imagen']
        widgets = {
            'password': forms.PasswordInput(),
        }
