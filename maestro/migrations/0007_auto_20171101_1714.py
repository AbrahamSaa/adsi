# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-02 00:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestro', '0006_auto_20171101_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asistencia',
            name='idDate',
        ),
        migrations.RemoveField(
            model_name='asistencia',
            name='idGrupo',
        ),
        migrations.RemoveField(
            model_name='asistencia',
            name='tipo',
        ),
    ]