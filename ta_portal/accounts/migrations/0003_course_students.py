# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-02-20 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200218_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.IntegerField(default=0),
        ),
    ]
