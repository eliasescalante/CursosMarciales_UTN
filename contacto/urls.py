from django.urls import path
from contacto import views
from contacto.views import Contacto

urlpatterns = [
    path('', Contacto.as_view(), name='contacto'),
]
