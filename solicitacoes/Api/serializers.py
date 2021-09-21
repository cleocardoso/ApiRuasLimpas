from rest_framework import serializers

from solicitacoes import models

class solicitacaoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.solicitacoes
        fields = ('__all__')