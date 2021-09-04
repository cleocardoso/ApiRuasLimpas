from msilib.schema import ListView

from rest_framework.decorators import action

import reclamacoes
import usuarios
from reclamacoes.models import Reclamacoes
from usuarios.models import usuario
from reclamacoes.serializers import reclamacoesSerializer


class ReclamacoesViewSet(viewsets.ModelViewSet):
    queryset = reclamacoes.objects.all()
    serializer_class = reclamacoesSerializer

    @action(methods=['get'], detail=False, url_path='listaReclamacoes')
    def listReclamacoes(self, request):
        id_str = "id"
        id = self.request.GET.get(id_str) or self.request.session[id_str]
        usuario = usuarios.objects.get(id=id)
        print("id-----"+id)
        reclamacao = Reclamacoes.objects.filter(usuario=usuario)

        context = {
            'reclamacao': reclamacao
        }
        return request, context

