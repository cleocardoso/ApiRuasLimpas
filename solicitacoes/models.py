from datetime import datetime

from django.db.models import Model, DateTimeField, ForeignKey, BooleanField, CASCADE

# Create your models here.
from django.utils import timezone

from reclamacoes.models import Reclamacoes


class Solicitacoes(Model):
    data = DateTimeField(null=True, blank=True, default=datetime.now(), name='data_solicitada')
    statusConcluido = BooleanField(null=True, name='status_concluido', blank=True, default=False)
    reclamacoes = ForeignKey(Reclamacoes,  CASCADE, name='reclamacoes', related_name='Reclamacoes')

    class Meta:
        db_table = 'solicitacoes'