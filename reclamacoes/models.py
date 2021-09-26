from datetime import datetime

from django.db import models
from django.utils import timezone

from usuarios.models import usuario
def upload_Image_reclamacoes(instance,filename):
    return f"{instance.usuario}-{filename}"

class Categoria(models.Model):

    LOAN_STATUS = (
        ('Lixo ', 'Lixo'),
        ('Entulhos de construção', 'Entulhos de construção'),
        ('Animais nas ruas', 'Animais nas ruas'),
        ('Poldar árvores', 'Poldar árvores'),
        ('Outros', 'Outros'),
    )
    nome = models.CharField(max_length=500, choices=LOAN_STATUS, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Reclamacoes(models.Model):
    data = models.DateTimeField(null=True, blank=True, default=datetime.now(), name='data_reclamacao')
    rua = models.CharField(max_length=10000)
    bairro = models.CharField(max_length=10000)
    descricao = models.CharField(max_length=10000)
    imagem = models.ImageField(upload_to=upload_Image_reclamacoes, blank=True, null=True)
    Usuario = models.ForeignKey(usuario, models.CASCADE, name='usuario', related_name='Usuario')
    categorias = models.ManyToManyField(Categoria, related_name='Categoria')
    trash = models.BooleanField(default=False)

    class Meta:
        db_table = 'reclamacoes'