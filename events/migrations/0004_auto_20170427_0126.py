# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-27 01:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20170427_0123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='event',
            name='all_day',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
