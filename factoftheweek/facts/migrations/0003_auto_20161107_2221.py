# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-07 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facts', '0002_auto_20161107_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fact',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='fact',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
