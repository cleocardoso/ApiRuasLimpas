from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from reclamacoes.Api.serializers import ReclamacoesSerializer, CategoriaSerializer
from reclamacoes.models import Reclamacoes, Categoria
from reclamacoes.serializers import categoriaSerializer, reclamacoesSerializer
from solicitacoes.Api.viewSets import list_by_user_trash
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

    #@action(methods=['get'], detail=False, url_path='listCategoria')
    def list(self,request):
       
        categorias = Categoria.objects.filter(trash=False).all()
        return Response(status=status.HTTP_200_OK, data=CategoriaSerializer(instance=categorias, many=True,
                                                context={'request': request}).data)

    @action(methods=['put'], detail=False, url_path='atualiza')
    def atualiza(self,request):
        print("OK")
        id_str = "id"
        id = request.GET.get(id_str)
        categoria = Categoria.objects.get(id=id)
        print(categoria)
        categoria.nome = request.data.get('nome')
        Categoria.save(categoria)
        return Response(status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='listLixeiraCategorias') 
    def listLixeiraCategorias(self,request):
        id_str = "id"
        id = request.GET.get(id_str)
        return Response(status=status.HTTP_200_OK, data=list_by_user_trash(id=id, trash=True, request=request))

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
        idUser=request.GET.get('idUser')
        user = usuario.objects.get(id=idUser)
        reclamacao = Reclamacoes.objects.filter(usuario=user, id=id).get()
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
    
    @action(methods=['get'], detail=False, url_path='total_por_mes_pelo_user')
    def total_por_mes_por_user(self, request):
        id=request.GET.get('id')
        try:
            user = usuario.objects.get(id=id)
            data = datetime.now()
            total = len(Reclamacoes.objects.filter(
                Q(data_reclamacao__month=data.month)
                & Q(data_reclamacao__year=data.year)
                & Q(usuario=user)
                & Q(trash=False)
            ).all())
            return Response(status=status.HTTP_200_OK, data={
                "size": total
            })
        except:
            return Response(status=status.HTTP_200_OK, data={
                "size": 0
            })