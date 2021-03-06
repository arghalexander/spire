# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 01:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_product', to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='MembershipProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('subscription', models.BooleanField(default=False)),
                ('membership_length', models.IntegerField(help_text='Length In Years')),
                ('membership_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership_product', to='members.MembershipLevel')),
            ],
        ),
    ]
