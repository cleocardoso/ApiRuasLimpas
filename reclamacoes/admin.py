from django.contrib import admin

# Register your models here.
from solicitacoes.models import Solicitacoes
from .models import *
# Register your models here.
admin.site.register(Reclamacoes)
admin.site.register(Categoria)
admin.site.register(Solicitacoes)