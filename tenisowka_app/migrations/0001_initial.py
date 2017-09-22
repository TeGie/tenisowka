# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-04 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TurniejWewnetrzny',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wynik_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Wynik_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Zawodnik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=128)),
                ('adres', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='wynik_2',
            name='zawodnik_2',
            field=models.ManyToManyField(to='tenisowka_app.Zawodnik'),
        ),
        migrations.AddField(
            model_name='wynik_1',
            name='zawodnik_1',
            field=models.ManyToManyField(to='tenisowka_app.Zawodnik'),
        ),
        migrations.AddField(
            model_name='turniejwewnetrzny',
            name='wynik_1',
            field=models.ManyToManyField(to='tenisowka_app.Wynik_1'),
        ),
        migrations.AddField(
            model_name='turniejwewnetrzny',
            name='wynik_2',
            field=models.ManyToManyField(to='tenisowka_app.Wynik_2'),
        ),
    ]
