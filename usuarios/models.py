from django.db import models
from django.contrib.auth.models import User


class usuario(models.Model):
    nome = models.CharField(max_length=255)
    sobreNome = models.CharField(max_length=255)
    cidade = models.CharField(max_length=10000)
    email = models.EmailField()
    senha = models.CharField(max_length=50)
    foto = models.ImageField(upload_to="user", blank=True, null=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):

        return str(self.id)

    class Meta:
        db_table = 'usuario'

