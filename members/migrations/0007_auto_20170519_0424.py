# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-19 04:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_auto_20170519_0420'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='preffered_name',
            new_name='preferred_name',
        ),
    ]
