# Generated by Django 3.2.7 on 2021-09-08 22:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacoes', '0003_alter_solicitacoes_data_solicitada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacoes',
            name='data_solicitada',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 8, 22, 15, 19, 740093, tzinfo=utc), null=True),
        ),
    ]