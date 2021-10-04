from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from reclamacoes.Api.serializers import ReclamacoesSerializer, CategoriaSerializer
from reclamacoes.models import Reclamacoes, Categoria
from reclamacoes.serializers import categoriaSerializer, reclamacoesSerializer
from solicitacoes.models import solicitacoes
from usuarios.models import usuario
from datetime import datetime
from django.db.models import Q

class categoriaViewsSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()

    @action(methods=['delete'], detail=False, url_path='deletarCategoria')         
    def deletarCategoria(self, request):
        id=request.GET.get('id')
        categoria = Categoria.objects.filter(id=id).get()
        categoria.trash = True
        Categoria.save(categoria)
        return Response(status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='listCategoria')
    def listCategoria(self,request):
        categoria_array = []
        id = "id"
        id = self.request.GET.get(id) or self.request.session[id]
        user = usuario.objects.get(id=id)
        categoria = Categoria.objects.filter(usuario=user, trash=False).order_by('id')
        for c in categoria:
            categoria(categoria=c,categoria_array=categoria_array, request=request)

        return categoria_array 

class ReclamacoesViewsSet(viewsets.ModelViewSet):
    serializer_class = ReclamacoesSerializer
    queryset = Reclamacoes.objects.all()

    #ele vai subreescrever esse metodo da class
    def create(self, request, *args, **kwargs):

        def get_categorias(ids):
            categorias = []
            for id in ids:
                categorias.append(Categoria.objects.get(id=id))
            return categorias
        reclamacoesReq = request.data
        categorias = get_categorias(reclamacoesReq['categorias'])
        print(categorias)
        reclamacoes = Reclamacoes.objects.create(rua=reclamacoesReq['rua'],
                                           bairro=reclamacoesReq['bairro'],
                                           imagem=reclamacoesReq['imagem'],
                                           descricao=reclamacoesReq['descricao'],
                                           usuario=usuario.objects.get(id=reclamacoesReq['usuario']))
        reclamacoes.categorias.set(categorias)
        Reclamacoes.save(reclamacoes)
        solicitacao = solicitacoes.objects.create(reclamacoes=reclamacoes)
        solicitacoes.save(solicitacao)
        return Response(status=status.HTTP_201_CREATED,
                        data=ReclamacoesSerializer(instance=reclamacoes,
                                                context={'request': request}).data)

    @action(methods=['get'], detail=False, url_path='listaReclamacoes')
    def listReclamacoes(self, request):
        id_str = "id"
        id = self.request.GET.get(id_str) or self.request.session[id_str]
        user = usuario.objects.get(id=id)
        reclamacao = Reclamacoes.objects.filter(usuario=user, trash=False).order_by('id')

        return Response(status=status.HTTP_200_OK,
                        data=reclamacoesSerializer(instance=reclamacao,
                                                many=True,
                                                context={'request': request}).data)

    @action(methods=['delete'], detail=False, url_path='deletarReclamacoes')         
    def deletarReclamacao(self, request):
        id=request.GET.get('id')
        reclamacao = Reclamacoes.objects.filter(id=id).get()
        #reclamacao.delete()
        reclamacao.trash = True
        Reclamacoes.save(reclamacao)
        return Response(status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='total_por_mes')
    def total_por_mes(self, request):
        data = datetime.now()
        total = len(Reclamacoes.objects.filter(
            Q(data_reclamacao__month=data.month)
            & Q(data_reclamacao__year=data.year)
        ).all())
        return Response(status=status.HTTP_200_OK, data={
            "size": total
        })