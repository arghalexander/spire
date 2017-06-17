# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 21:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spiresite', '0028_auto_20170614_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpricing',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_pricing', to='events.Event'),
        ),
    ]