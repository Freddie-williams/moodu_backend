# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0011_auto_20161017_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
