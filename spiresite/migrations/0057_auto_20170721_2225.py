# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 22:25
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spiresite', '0056_auto_20170717_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='halloffameoverviewpage',
            name='event',
        ),
        migrations.AddField(
            model_name='halloffameoverviewpage',
            name='button_one_text',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='halloffameoverviewpage',
            name='button_one_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='halloffameoverviewpage',
            name='button_two_text',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='halloffameoverviewpage',
            name='button_two_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='halloffameoverviewpage',
            name='event_text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
