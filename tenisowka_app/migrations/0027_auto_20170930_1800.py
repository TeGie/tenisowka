# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-30 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenisowka_app', '0026_auto_20170930_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='player',
        ),
        migrations.AddField(
            model_name='attendance',
            name='player',
            field=models.ManyToManyField(to='tenisowka_app.Player', verbose_name='Zawodnik'),
        ),
    ]