from datetime import datetime

from django.db import models

# Create your models here.
from django.utils import timezone

from reclamacoes.models import Reclamacoes


class solicitacoes(models.Model):
    data = models.DateTimeField(null=True, blank=True, default=datetime.now(), name='data_solicitada')
    statusConcluido = models.BooleanField(null=True, name='status_concluido', blank=True, default=False)
    reclamacoes = models.ForeignKey(Reclamacoes,  models.CASCADE, name='reclamacoes', related_name='Reclamacoes')

    class Meta:
        db_table = 'solicitacoes'