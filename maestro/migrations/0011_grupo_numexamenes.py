# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-15 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maestro', '0010_calificacion_calificacionalumno'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='numExamenes',
            field=models.SmallIntegerField(null=True),
        ),
    ]
