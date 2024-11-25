from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render
from contacto.models import Consulta
from contacto.forms import ConsultaForm
from django.views.generic import FormView

# https://docs.djangoproject.com/es/3.2/topics/class-based-views/generic-editing/

class Contacto(FormView):
    """
    Vista para el formulario de contacto
    """
    template_name = "contacto/contacto.html"
    form_class = ConsultaForm
    success_url = "mensaje_enviado"

    def form_valid(self, form):
        form.save()
        form.send_email()
        return super().form_valid(form)


class MensajeEnviado(View):
    """
    Vista para el mensaje de que el mensaje ha sido enviado
    """
    template = "contacto/mensaje_enviado.html"

    def get(self, request):
        form = ConsultaForm()
        params = {}
        params["form"] = form
        return render(request, self.template, params)
