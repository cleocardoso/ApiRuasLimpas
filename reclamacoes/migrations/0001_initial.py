# Generated by Django 3.2.6 on 2021-08-29 00:04

from django.db import migrations, models
import django.db.models.deletion


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
            ],
        ),
        migrations.CreateModel(
            name='Reclamacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_reclamacao', models.DateField(blank=True, null=True)),
                ('bairro', models.CharField(max_length=10000)),
                ('descricao', models.CharField(max_length=10000)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Usuario', to='usuarios.usuario')),
            ],
            options={
                'db_table': 'reclamacoes',
            },
        ),
    ]
