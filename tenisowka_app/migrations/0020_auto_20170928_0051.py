# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-28 00:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenisowka_app', '0019_zawodnik_elo_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='nazwa')),
                ('description', models.TextField(blank=True, null=True, verbose_name='opis')),
                ('start', models.DateTimeField(null=True)),
                ('end', models.DateTimeField(null=True, verbose_name='koniec')),
            ],
            options={
                'verbose_name': 'Wydarzenie',
                'verbose_name_plural': 'Wydarzenia',
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_pl_1', models.SmallIntegerField(default=0, verbose_name='wynik zawodnika 1')),
                ('result_pl_2', models.SmallIntegerField(default=0, verbose_name='wynik zawodnika 2')),
                ('date', models.DateField(verbose_name='data')),
            ],
            options={
                'verbose_name': 'Pojedynek',
                'verbose_name_plural': 'Pojedynki',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Imię i nazwisko')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='data urodzenia')),
                ('adress', models.CharField(blank=True, max_length=128, verbose_name='adres')),
                ('med_check_date', models.DateField(blank=True, null=True, verbose_name='data badania')),
                ('licence_number', models.IntegerField(blank=True, null=True, verbose_name='nr licencji')),
                ('elo_rating', models.IntegerField(default=1200)),
            ],
            options={
                'verbose_name': 'Zawodnik',
                'verbose_name_plural': 'Zawodnicy',
            },
        ),
        migrations.RemoveField(
            model_name='pojedynek',
            name='zawodnik_1',
        ),
        migrations.RemoveField(
            model_name='pojedynek',
            name='zawodnik_2',
        ),
        migrations.DeleteModel(
            name='Wydarzenie',
        ),
        migrations.DeleteModel(
            name='Pojedynek',
        ),
        migrations.DeleteModel(
            name='Zawodnik',
        ),
        migrations.AddField(
            model_name='match',
            name='player_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_1', to='tenisowka_app.Player', verbose_name='zawodnik 1'),
        ),
        migrations.AddField(
            model_name='match',
            name='player_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_2', to='tenisowka_app.Player', verbose_name='zawodnik 2'),
        ),
    ]
