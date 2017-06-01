# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 04:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
        ('spiresite', '0030_auto_20170531_0350'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberDirectoryPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]