from django.db import models

# Create your models here.
from reclamacoes.models import Reclamacoes


class Solicitacoes(models.Model):
    data = models.DateField(null=True, blank=True, name='data_solicitada')
    statusConcluido = models.BooleanField(null=True, name='status_concluido', blank=True, default=False)
    reclamacoes = models.ForeignKey(Reclamacoes,  models.CASCADE, name='reclamacoes', related_name='Reclamacoes')

    class Meta:
        db_table = 'solicitacoes'