# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 09:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_auto_20170219_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 9, 10, 50, 287429, tzinfo=utc)),
        ),
    ]
