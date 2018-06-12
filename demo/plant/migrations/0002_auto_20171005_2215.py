# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-05 16:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actuator_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Water_Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_level', models.FloatField(default=0)),
                ('time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='actuator',
            name='status',
        ),
        migrations.RemoveField(
            model_name='water_body',
            name='water_level',
        ),
        migrations.AlterField(
            model_name='actuator',
            name='plant_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='actuator',
            name='wb_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='water_level',
            name='wb_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plant.Water_Body'),
        ),
        migrations.AddField(
            model_name='actuator_status',
            name='ac_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plant.Actuator'),
        ),
    ]