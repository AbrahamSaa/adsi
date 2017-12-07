# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-20 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maestro', '0012_metricasgroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='calificacionAlumnoProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.IntegerField()),
                ('idGrupo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='calificacionProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCalif', models.IntegerField()),
                ('idAlumno', models.IntegerField()),
                ('calif', models.IntegerField()),
            ],
        ),
    ]
