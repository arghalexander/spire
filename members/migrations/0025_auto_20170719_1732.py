# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 17:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0024_remove_member_skills_specialties'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='memberprofesionalinformation',
            options={'verbose_name_plural': 'Member Professional Information'},
        ),
        migrations.AlterModelOptions(
            name='memberpurchasehistory',
            options={'verbose_name_plural': 'Member Purchases'},
        ),
    ]
