from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from reclamacoes import views

app_name = 'reclamacoes'
urlpatterns = [
    #path('listaReclamacoes/<str:id>', views.listReclamacoes,name='listReclamacoes'),
]