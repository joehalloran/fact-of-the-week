# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-12 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facts', '0003_auto_20161107_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='fact',
            name='send_email_on_publish',
            field=models.BooleanField(default=False),
        ),
    ]