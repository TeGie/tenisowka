# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-30 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenisowka_app', '0025_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='present',
            field=models.BooleanField(),
        ),
    ]
