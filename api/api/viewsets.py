from rest_framework import viewsets
from api.api import serializers
from api import models

class ApiViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ApiSerializer
    queryset = models.Usuario.objects.all()