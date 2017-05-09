# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-05 19:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_remove_event_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_attendance', to='events.Event')),
            ],
        ),
        migrations.AlterField(
            model_name='eventpricinglevel',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_pricing', to='events.Event'),
        ),
    ]
