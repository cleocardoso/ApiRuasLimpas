# Generated by Django 3.2.7 on 2021-09-08 22:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reclamacoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reclamacoes',
            name='data_reclamacao',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 8, 19, 13, 23, 446641), null=True),
        ),
    ]