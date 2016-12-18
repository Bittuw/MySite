# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-18 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Conserts', '0002_auto_20161218_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consert',
            name='image_path',
        ),
        migrations.AddField(
            model_name='consert',
            name='image',
            field=models.ImageField(default='Conserts/defaults/default.png', upload_to='image'),
        ),
    ]
