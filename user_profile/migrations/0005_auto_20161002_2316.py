# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-02 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_userprofile_refresh_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='access_token',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='refresh_token',
            field=models.CharField(default='', max_length=500),
        ),
    ]
