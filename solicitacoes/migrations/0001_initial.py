# Generated by Django 3.2.7 on 2021-09-26 17:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reclamacoes', '0010_auto_20210926_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='solicitacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_solicitada', models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 26, 14, 4, 57, 398921), null=True)),
                ('status_concluido', models.BooleanField(blank=True, default=False, null=True)),
                ('reclamacoes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reclamacoes', to='reclamacoes.reclamacoes')),
            ],
            options={
                'db_table': 'solicitacoes',
            },
        ),
    ]
