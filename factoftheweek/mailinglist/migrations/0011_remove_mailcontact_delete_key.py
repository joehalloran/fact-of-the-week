# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-27 21:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailinglist', '0010_auto_20161127_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailcontact',
            name='delete_key',
        ),
    ]
