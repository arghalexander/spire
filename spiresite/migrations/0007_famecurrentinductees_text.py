# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 00:07
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spiresite', '0006_auto_20170609_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='famecurrentinductees',
            name='text',
            field=wagtail.wagtailcore.fields.RichTextField(default='test'),
            preserve_default=False,
        ),
    ]
