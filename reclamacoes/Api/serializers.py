from rest_framework import serializers

from reclamacoes import models


class ReclamacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reclamacoes
        fields = ('__all__')

