# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-08 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpDesk', '0002_auto_20160708_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='rif',
            field=models.CharField(max_length=100),
        ),
    ]
