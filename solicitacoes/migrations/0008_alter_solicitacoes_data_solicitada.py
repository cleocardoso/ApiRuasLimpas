# Generated by Django 3.2.7 on 2021-09-11 00:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacoes', '0007_alter_solicitacoes_data_solicitada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacoes',
            name='data_solicitada',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 10, 21, 25, 26, 181431), null=True),
        ),
    ]
