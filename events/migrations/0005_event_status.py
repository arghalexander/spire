# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-16 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20170516_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('PUBLISHED', 'Published'), ('DRAFT', 'Draft')], default='DRAFT', max_length=254),
        ),
    ]