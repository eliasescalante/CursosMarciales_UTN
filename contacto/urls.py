from django.urls import path
from contacto import views
from contacto.views import Contacto
from contacto.views import MensajeEnviado

#Rutas de app contacto
urlpatterns = [
    path('', Contacto.as_view(), name='contacto'),
    path('mensaje_enviado', MensajeEnviado.as_view(), name='mensaje_emviado'),
]
