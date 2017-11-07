# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-05 16:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_series', '0005_auto_20171020_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='episode',
            old_name='tv_season',
            new_name='season',
        ),
        migrations.RenameField(
            model_name='season',
            old_name='nb_episodes',
            new_name='nb_of_episodes',
        ),
        migrations.RenameField(
            model_name='tvshow',
            old_name='in_production',
            new_name='is_in_production',
        ),
        migrations.RenameField(
            model_name='tvshow',
            old_name='nb_season',
            new_name='nb_of_seasons',
        ),
        migrations.RemoveField(
            model_name='episode',
            name='tmdb_id',
        ),
        migrations.RemoveField(
            model_name='season',
            name='tmdb_id',
        ),
    ]