# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-16 19:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facts', '0004_fact_send_email_on_publish'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fact',
            old_name='send_email_on_publish',
            new_name='send_email_on_save',
        ),
    ]
