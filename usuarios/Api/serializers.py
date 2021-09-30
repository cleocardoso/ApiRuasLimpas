from rest_framework import serializers
from django.contrib.auth.models import User
from usuarios import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True},
            'senha': {'write_only': True}
        }
        model = User
        #fields = ('id', 'nome','sobreNome', 'email', 'senha', 'cidade', 'foto', 'active')
        fields = ('__all__')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True},
            'senha': {'write_only': True}
        }
        model = models.usuario
        #fields = ('id', 'nome','sobreNome', 'email', 'senha', 'cidade', 'foto', 'active')
        fields = ('__all__')


