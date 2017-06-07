# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 20:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
        ('spiresite', '0039_auto_20170606_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeadershipRegionalLeadersfPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.CharField(blank=True, max_length=255)),
                ('body', wagtail.wagtailcore.fields.StreamField([('region', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('leader', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([('name', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('company', wagtail.wagtailcore.blocks.CharBlock())])))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
