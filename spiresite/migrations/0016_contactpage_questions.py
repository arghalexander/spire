# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 19:33
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spiresite', '0015_auto_20170609_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='questions',
            field=wagtail.wagtailcore.fields.RichTextField(default='1'),
            preserve_default=False,
        ),
    ]