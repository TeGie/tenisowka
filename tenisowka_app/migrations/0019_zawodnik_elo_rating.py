# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-27 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenisowka_app', '0018_auto_20170927_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='zawodnik',
            name='elo_rating',
            field=models.IntegerField(default=1200),
        ),
    ]
