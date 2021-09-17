from reclamacoes.Api.serializers import ReclamacoesSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from reclamacoes.models import Reclamacoes
from solicitacoes.models import Solicitacoes
from solicitacoes.Api import serializers
from usuarios.models import usuario


class SolicitacoesViewsSet(viewsets.ModelViewSet):
    serializer_class = serializers.solicitacaoesSerializer
    queryset = Solicitacoes.objects.all()

    @action(methods=['get'], detail=False, url_path='listaSolicitacoes')
    def list_by_user(self, request):
        solicitacoes_array = []
        id_str = "id"
        id = self.request.GET.get(id_str) or self.request.session[id_str]
        user = usuario.objects.get(id=id)
        reclamacoes = Reclamacoes.objects.filter(usuario=user).order_by('id')

        def get_solicitacao(reclamacoes):
            solicitacao_by_user = Solicitacoes.objects.filter(reclamacoes=reclamacoes.id).first()
            #for s in solicitacao_by_user:
            #    print(s)
            if solicitacao_by_user:
                data = {
                    "data": solicitacao_by_user.data_solicitada,
                    "statusConcluido": solicitacao_by_user.status_concluido,
                    "reclamacoes": ReclamacoesSerializer(instance=reclamacoes,
                                                context={'request': request}).data
                }
                solicitacoes_array.append(data)
            

        for r in reclamacoes:
            get_solicitacao(r)

        return Response(status=status.HTTP_200_OK, data=solicitacoes_array)
