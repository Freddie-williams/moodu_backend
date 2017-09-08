# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-09 16:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('spotify_id', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('title', models.TextField()),
                ('message', models.TextField()),
                ('locked', models.BooleanField()),
                ('public', models.BooleanField()),
                ('playlist_image', models.ImageField(null=True, upload_to=b'user_uploads')),
                ('playlist_video', models.FileField(null=True, upload_to=b'video')),
                ('latitude', models.TextField()),
                ('longitude', models.TextField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL)),
                ('shared_with_users', models.ManyToManyField(related_name='shared_with', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('spotify_id', models.TextField()),
                ('track_preview_url', models.URLField()),
                ('album_artwork', models.URLField()),
                ('album_title', models.TextField()),
                ('artists', models.ManyToManyField(to='music.Artist')),
            ],
        ),
        migrations.AddField(
            model_name='playlist',
            name='song_list',
            field=models.ManyToManyField(to='music.Song'),
        ),
    ]
