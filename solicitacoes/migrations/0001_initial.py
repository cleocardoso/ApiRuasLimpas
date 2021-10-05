# Generated by Django 3.2.7 on 2021-10-05 02:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reclamacoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='solicitacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_solicitada', models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 4, 23, 15, 29, 617247), null=True)),
                ('status_concluido', models.BooleanField(blank=True, default=False, null=True)),
                ('reclamacoes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reclamacoes', to='reclamacoes.reclamacoes')),
            ],
            options={
                'db_table': 'solicitacoes',
            },
        ),
    ]
