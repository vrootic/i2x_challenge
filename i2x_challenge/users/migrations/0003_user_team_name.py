# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-18 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170518_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='team_name',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]
