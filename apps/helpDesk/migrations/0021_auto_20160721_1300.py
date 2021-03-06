# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-21 17:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpDesk', '0020_auto_20160719_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='nombre_encargador',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bitacora',
            name='comentario',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bitacora',
            name='id_estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='helpDesk.Estados'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bitacora',
            name='monto',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='numero',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
