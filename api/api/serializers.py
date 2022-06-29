from rest_framework import serializers
from api import models

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = '__all__'       
