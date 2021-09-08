# Generated by Django 3.2.7 on 2021-09-04 16:19

from django.db import migrations, models
import django.db.models.deletion
import reclamacoes.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, choices=[('Lixo ', 'Lixo'), ('Entulhos de construção', 'Entulhos de construção'), ('Animais nas ruas', 'Animais nas ruas'), ('Poldar árvores', 'Poldar árvores'), ('Outros', 'Outros')], max_length=500)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Reclamacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_reclamacao', models.DateField(blank=True, null=True)),
                ('bairro', models.CharField(max_length=10000)),
                ('descricao', models.CharField(max_length=10000)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to=reclamacoes.models.upload_Image_reclamacoes)),
                ('categorias', models.ManyToManyField(related_name='Categoria', to='reclamacoes.Categoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Usuario', to='usuarios.usuario')),
            ],
            options={
                'db_table': 'reclamacoes',
            },
        ),
    ]