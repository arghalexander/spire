# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-10 17:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0022_auto_20170509_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberIndustry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry', models.CharField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='membereducation',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='members.Member'),
        ),
        migrations.AddField(
            model_name='member',
            name='industry',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='member_industry', to='members.MemberIndustry'),
            preserve_default=False,
        ),
    ]