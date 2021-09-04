from msilib.schema import ListView

import reclamacoes
from reclamacoes.models import Reclamacoes
from reclamacoes.serializers import reclamacoesSerializer


class ReclamacoesViewSet(viewsets.ModelViewSet):
    queryset = reclamacoes.objects.all()
    serializer_class = reclamacoesSerializer


