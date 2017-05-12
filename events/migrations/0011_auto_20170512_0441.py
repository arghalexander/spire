# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-12 04:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20170511_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventattendance',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_instance', to='events.Event'),
        ),
    ]
