# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 01:01
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spiresite', '0007_famecurrentinductees_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='famepreviousinductees',
            name='bio',
            field=wagtail.wagtailcore.fields.RichTextField(default='test'),
            preserve_default=False,
        ),
    ]