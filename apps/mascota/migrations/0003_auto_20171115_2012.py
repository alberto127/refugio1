# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-15 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0002_auto_20171115_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='vacuna',
            field=models.ManyToManyField(blank=True, to='mascota.Vacuna'),
        ),
    ]