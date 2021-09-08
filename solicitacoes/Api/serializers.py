from rest_framework import serializers

from solicitacoes import models

class solicitacaoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Solicitacoes
        fields = ('__all__')