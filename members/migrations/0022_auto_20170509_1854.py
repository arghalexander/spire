# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-09 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0021_membernote_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MemberDegree',
            new_name='MemberEducation',
        ),
        migrations.AlterField(
            model_name='membernote',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
