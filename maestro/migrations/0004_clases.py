# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-22 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maestro', '0003_alumnos'),
    ]

    operations = [
        migrations.CreateModel(
            name='clases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idAlumno', models.SmallIntegerField()),
                ('idClase', models.SmallIntegerField()),
            ],
        ),
    ]
