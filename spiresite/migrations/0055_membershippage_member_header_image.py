# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-13 23:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('spiresite', '0054_auto_20170703_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='membershippage',
            name='member_header_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='member_header_image', to='wagtailimages.Image'),
        ),
    ]
