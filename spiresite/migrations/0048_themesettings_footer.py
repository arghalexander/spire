# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-23 20:35
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spiresite', '0047_coresponsors'),
    ]

    operations = [
        migrations.AddField(
            model_name='themesettings',
            name='footer',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
