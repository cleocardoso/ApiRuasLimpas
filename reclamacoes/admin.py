from django.contrib import admin

# Register your models here.
from .models import Reclamacoes, Categoria
# Register your models here.
admin.site.register(Reclamacoes)
admin.site.register(Categoria)