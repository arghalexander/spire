# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-05 18:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0013_auto_20170505_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberaddress',
            name='address',
        ),
    ]
