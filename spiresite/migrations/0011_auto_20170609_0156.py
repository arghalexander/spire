# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 01:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
        ('spiresite', '0010_auto_20170609_0139'),
    ]

    operations = [
        migrations.CreateModel(
            name='HallOfFameStandardPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.CharField(blank=True, max_length=255)),
                ('body', wagtail.wagtailcore.fields.StreamField([('text', wagtail.wagtailcore.blocks.RichTextBlock())])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='halloffamebanquetspage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('image_block', wagtail.wagtailcore.blocks.StructBlock([(b'image_one', wagtail.wagtailimages.blocks.ImageChooserBlock(null=True)), (b'image_two', wagtail.wagtailimages.blocks.ImageChooserBlock(null=True))])), ('gallery_block', wagtail.wagtailcore.blocks.StructBlock([(b'caption', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'images', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(null=True))])))]))], null=True),
        ),
    ]
