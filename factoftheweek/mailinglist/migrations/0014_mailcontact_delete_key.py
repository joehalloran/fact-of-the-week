# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-27 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailinglist', '0013_remove_mailcontact_delete_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailcontact',
            name='delete_key',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
