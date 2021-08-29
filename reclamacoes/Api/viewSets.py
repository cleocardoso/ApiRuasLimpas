from rest_framework import viewsets
from reclamacoes.Api import serializers
from reclamacoes import models

class ReclamacoesViewsSet(viewsets.ModelViewSet):
    serializer_class = serializers.ReclamacoesSerializer
    queryset = models.Reclamacoes.objects.all()