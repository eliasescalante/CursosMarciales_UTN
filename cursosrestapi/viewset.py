from rest_framework import viewsets
from .models import CursosRestApi
from .serializer import CursosRestApiSerializer

class CursosRestApiViewSet(viewsets.ModelViewSet):
    queryset = CursosRestApi.objects.all()
    serializer_class = CursosRestApiSerializer