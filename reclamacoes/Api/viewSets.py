from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from reclamacoes.Api import serializers
from reclamacoes import models
from reclamacoes.models import Reclamacoes
from reclamacoes.serializers import reclamacoesSerializer
from usuarios.models import usuario


class ReclamacoesViewsSet(viewsets.ModelViewSet):
    serializer_class = serializers.ReclamacoesSerializer
    queryset = models.Reclamacoes.objects.all()

    @action(methods=['get'], detail=False, url_path='listaReclamacoes')
    def listReclamacoes(self, request):
        id_str = "id"
        id = self.request.GET.get(id_str) or self.request.session[id_str]
        user = usuario.objects.get(id=id)

        reclamacao = Reclamacoes.objects.filter(usuario=user).order_by('id')

        return Response(status=status.HTTP_200_OK,
                        data=reclamacoesSerializer(instance=reclamacao,
                                                many=True,
                                                context={'request': request}).data)