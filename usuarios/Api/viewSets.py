from rest_framework import viewsets
from usuarios.Api import serializers
from usuarios import models

class UsuariosViewsSet(viewsets.ModelViewSet):
    serializer_class = serializers.UsuarioSerializer
    queryset = models.usuario.objects.all()