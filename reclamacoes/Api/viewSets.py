from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from reclamacoes.Api import serializers
from reclamacoes import models
from reclamacoes.Api.serializers import ReclamacoesSerializer
from reclamacoes.models import Reclamacoes, Categoria
from reclamacoes.serializers import reclamacoesSerializer
from solicitacoes.models import Solicitacoes
from usuarios.models import usuario


class ReclamacoesViewsSet(viewsets.ModelViewSet):
    serializer_class = serializers.ReclamacoesSerializer
    queryset = models.Reclamacoes.objects.all()

    #ele vai subreescrever esse metodo da class
    def create(self, request, *args, **kwargs):

        def get_categorias(ids):
            categorias = []
            for id in ids:
                categorias.append(Categoria.objects.get(id=id))
            return categorias
        reclamacoesReq = request.data
        categorias = get_categorias(reclamacoesReq['categorias'])
        print(categorias)
        reclamacoes = Reclamacoes.objects.create(rua=reclamacoesReq['rua'],
                                           bairro=reclamacoesReq['bairro'],
                                           imagem=reclamacoesReq['imagem'],
                                           descricao=reclamacoesReq['descricao'],
                                           usuario=usuario.objects.get(id=reclamacoesReq['usuario']))
        reclamacoes.categorias.set(categorias)
        Reclamacoes.save(reclamacoes)
        solicitacao = Solicitacoes.objects.create(reclamacoes=reclamacoes)
        Solicitacoes.save(solicitacao)
        return Response(status=status.HTTP_201_CREATED,
                        data=ReclamacoesSerializer(instance=reclamacoes,
                                                context={'request': request}).data)

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