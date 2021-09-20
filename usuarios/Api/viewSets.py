from rest_framework import viewsets, request, status
from rest_framework.decorators import action
from rest_framework.response import Response

import usuarios
from usuarios.Api import serializers
from usuarios.Api.serializers import UsuarioSerializer
from usuarios.models import usuario


class UsuariosViewsSet(viewsets.ModelViewSet):
    serializer_class = serializers.UsuarioSerializer
    queryset = usuario.objects.all()

    @action(methods=['post'], detail=False, url_path='login')
    def create_login(self, request):
        email = request.data.get('email')
        senha = request.data.get('senha')

        def get_user(user):
            is_admin = user.user is not None
            data = {
                "user": UsuarioSerializer(instance=user,
                                                       context={'request': request}).data,
                "is_admin": is_admin
            }
            return Response(status=status.HTTP_200_OK,
                            data=data)


        try:
            user = usuario.objects.get(email=email, senha=senha)
            if user:
                return get_user(user)
        except:
            print()
        return Response(status=status.HTTP_404_NOT_FOUND)
