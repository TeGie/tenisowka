# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-06 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenisowka_app', '0009_auto_20170906_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pojedynek',
            name='set_1_zaw_1',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pojedynek',
            name='set_1_zaw_2',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='pojedynek',
            name='set_2_zaw_1',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='pojedynek',
            name='set_2_zaw_2',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='pojedynek',
            name='set_3_zaw_1',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='pojedynek',
            name='set_3_zaw_2',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='pojedynek',
            name='set_4_zaw_1',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='pojedynek',
            name='set_4_zaw_2',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='pojedynek',
            name='set_5_zaw_1',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='pojedynek',
            name='set_5_zaw_2',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='pojedynek',
            name='wynik_zaw_1',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='pojedynek',
            name='wynik_zaw_2',
            field=models.SmallIntegerField(default=0, null=True),
        ),
    ]
