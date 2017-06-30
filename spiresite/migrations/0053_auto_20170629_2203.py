# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-29 22:03
from __future__ import unicode_literals

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('spiresite', '0052_auto_20170629_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardleadershippage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('three_columnn_block', wagtail.wagtailcore.blocks.StructBlock([(b'one', wagtail.wagtailcore.blocks.RichTextBlock()), (b'two', wagtail.wagtailcore.blocks.RichTextBlock()), (b'three', wagtail.wagtailcore.blocks.RichTextBlock())]))]),
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('button', wagtail.wagtailcore.blocks.StructBlock([(b'link', wagtail.wagtailcore.blocks.URLBlock()), (b'label', wagtail.wagtailcore.blocks.CharBlock())])), ('people_list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(null=True)), (b'name', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'description', wagtail.wagtailcore.blocks.RichTextBlock())]), icon='group', template='spiresite/blocks/people_list.html')), ('redirect', wagtail.wagtailcore.blocks.StructBlock([(b'page', wagtail.wagtailcore.blocks.PageChooserBlock())]))]),
        ),
    ]