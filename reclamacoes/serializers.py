from rest_framework import serializers

from .models import Reclamacoes,Categoria


class reclamacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reclamacoes
        fields = ('__all__')
