# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-16 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiresite', '0002_remove_eventpricing_free'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpricing',
            name='ticket_quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
