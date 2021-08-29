from django.db import models

# Create your models here.
from usuarios.models import usuario


class Categoria(models.Model):
    #user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    LOAN_STATUS = (
        ('Lixo ', 'Lixo'),
        ('Entulhos de construção', 'Entulhos de construção'),
        ('Animais nas ruas', 'Animais nas ruas'),
        ('Poldar árvores', 'Poldar árvores'),
        ('Outros', 'Outros'),
    )
class Reclamacoes(models.Model):
    data = models.DateField(null=True, blank=True, name='data_reclamacao')
    bairro = models.CharField(max_length=10000)
    descricao = models.CharField(max_length=10000)
    imagem = models.ImageField(upload_to="user", blank=True, null=True)
    Usuario = models.ForeignKey(usuario, models.CASCADE, name='usuario', related_name='Usuario')



    class Meta:
        db_table = 'reclamacoes'