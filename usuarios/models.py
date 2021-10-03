from datetime import datetime
from uuid import uuid4

from django.db import models
from django.contrib.auth.models import User

def upload_Image_user(instance,filename):
    return f"{instance.id}-{filename}"

class usuario(models.Model):
    #id_user = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    nome = models.CharField(max_length=255)
    sobreNome = models.CharField(max_length=255)
    cidade = models.CharField(max_length=10000)
    email = models.EmailField()
    senha = models.CharField(max_length=50)
    foto = models.ImageField(upload_to=upload_Image_user, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateTimeField(null=True, blank=True, default=datetime.now(), name='data_criacao')
    ultimo_acesso = models.DateTimeField(null=True, blank=True, name='data_ultimo_acesso')

    def __str__(self):

        return str(self.id)

    class Meta:
        db_table = 'usuario'