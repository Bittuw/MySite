# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-18 12:37
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consert',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('theatre', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=100)),
                (
                    'time',
                    models.DateTimeField(
                        default=datetime.datetime(
                            2016, 12, 18, 12, 37, 45, 853800,
                            tzinfo=utc
                            )
                        )
                    ),
                (
                    'image_path',
                    models.FilePathField(
                        null=True,
                        path='images/'
                        )
                    ),
                (
                    'reservation',
                    models.ManyToManyField(
                        to=settings.AUTH_USER_MODEL
                        )
                    ),
            ],
        ),
    ]
