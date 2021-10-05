from reclamacoes.Api.serializers import ReclamacoesSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from reclamacoes.models import Reclamacoes
from solicitacoes.models import solicitacoes
from solicitacoes.Api import serializers
from usuarios.models import usuario

def get_solicitacao(reclamacoes, solicitacoes_array, request):
            solicitacao_by_user = solicitacoes.objects.filter(reclamacoes=reclamacoes.id).first()
            #for s in solicitacao_by_user:
            #    print(s)
            if solicitacao_by_user:
                data = {
                    "id": solicitacao_by_user.id,
                    "data": solicitacao_by_user.data_solicitada,
                    "statusConcluido": solicitacao_by_user.status_concluido,
                    "reclamacoes": ReclamacoesSerializer(instance=reclamacoes,
                                                context={'request': request}).data
                }
                solicitacoes_array.append(data)

def list_by_user_trash(id, trash, request):
        solicitacoes_array = []
        user = usuario.objects.get(id=id)
        reclamacoes = Reclamacoes.objects.filter(usuario=user, trash=trash).order_by('id')

        for r in reclamacoes:
            get_solicitacao(reclamacoes=r, solicitacoes_array=solicitacoes_array, request=request)

        return solicitacoes_array 

class SolicitacoesViewsSet(viewsets.ModelViewSet):
    serializer_class = serializers.solicitacaoesSerializer
    queryset = solicitacoes.objects.all()

    #ele vai subreescrever esse metodo da class
    def list(self, request, *args, **kwargs):
        solicitacoes_array = []
        reclamacoes = Reclamacoes.objects.all()

        for r in reclamacoes:
            get_solicitacao(reclamacoes=r, solicitacoes_array=solicitacoes_array, request=request)

        return Response(status=status.HTTP_200_OK, data=solicitacoes_array)

    @action(methods=['get'], detail=False, url_path='listaSolicitacoes')
    def list_by_user(self, request):
        id_str = "id"
        id = request.GET.get(id_str)
        data = list_by_user_trash(id=id, trash=False, request=request)
        return Response(status=status.HTTP_200_OK, data=data)

    @action(methods=['put'], detail=False, url_path='atualizarSolicitacoes')
    def atualizarSolicitacoes(self, request):
        def str2bool(v):
            return v.lower() in ("yes", "true", "t", "1")

        id_str = "id"
        id = request.GET.get(id_str)
        status_data = request.data
        s = solicitacoes.objects.filter(id=id).get()
        s.status_concluido = str2bool(status_data['status_concluido'])
        solicitacoes.save(s)
        return Response(status=status.HTTP_200_OK)


    @action(methods=['get'], detail=False, url_path='listLixeiraReclamacoes') 
    def listLixeiraReclamacoes(self,request):
        id_str = "id"
        id = request.GET.get(id_str)
        return Response(status=status.HTTP_200_OK, data=list_by_user_trash(id=id, trash=True, request=request))
