# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-13 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idMaestro', models.IntegerField()),
                ('materia', models.CharField(max_length=35)),
                ('aula', models.CharField(max_length=10)),
                ('cupo', models.SmallIntegerField()),
                ('carrera', models.CharField(max_length=25)),
                ('horaInicio', models.CharField(max_length=10)),
                ('horaFinal', models.CharField(max_length=10)),
                ('dias', models.CharField(max_length=100)),
            ],
        ),
    ]