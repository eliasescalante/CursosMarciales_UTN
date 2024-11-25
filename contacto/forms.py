from django import forms
from django.forms import ModelForm
from contacto.models import Consulta
from django import forms
from captcha.fields import CaptchaField
from datetime import datetime

class ConsultaForm(ModelForm):
    """
    Formulario para crear consultas
    """
    captcha = CaptchaField()

    class Meta:
        model = Consulta
        fields = [
            "nombre",
            "descripcion",
            "mail",
            "telefono",
        ]

    def send_email(self):
        """
        Envia un correo electrónico con la información de la consulta
        """

        nombre = self.cleaned_data["nombre"]
        descripcion = self.cleaned_data["descripcion"]
        mail = self.cleaned_data["mail"]
        telefono = self.cleaned_data["telefono"]

        fecha = datetime.now().date()
        estado_respuesta = "No contestada"
        
        print("enviando datos")
        print(nombre, descripcion, mail, estado_respuesta, telefono, fecha)
