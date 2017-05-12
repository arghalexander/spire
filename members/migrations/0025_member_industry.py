# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-10 21:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0024_remove_member_industry'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='industry',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_industry', to='members.MemberIndustry'),
        ),
    ]
