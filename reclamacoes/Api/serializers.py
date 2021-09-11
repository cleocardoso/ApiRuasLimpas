from rest_framework import serializers

from reclamacoes import models
from reclamacoes.models import Categoria


class ReclamacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reclamacoes
        fields = ('__all__')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')
