# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-05 16:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_auto_20170427_0123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='cell_phone',
            new_name='mobile_phone',
        ),
    ]
