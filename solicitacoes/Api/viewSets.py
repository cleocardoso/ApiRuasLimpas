from rest_framework import viewsets
from solicitacoes import models
from solicitacoes.Api import serializers


class SolicitacoesViewsSet(viewsets.ModelViewSet):
    serializer_class = serializers.solicitacaoesSerializer
    queryset = models.Solicitacoes.objects.all()