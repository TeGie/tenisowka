# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-28 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenisowka_app', '0022_auto_20170928_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='elo_rating',
            field=models.SmallIntegerField(default=1200),
        ),
    ]