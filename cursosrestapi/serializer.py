from .models import CursosRestApi
from rest_framework import serializers

class CursosRestApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursosRestApi
        fields = '__all__'