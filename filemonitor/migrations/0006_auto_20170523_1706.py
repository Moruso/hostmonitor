# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemonitor', '0005_auto_20170523_1541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actualfile',
            old_name='status',
            new_name='ckstatus',
        ),
        migrations.AddField(
            model_name='actualfile',
            name='dlstatus',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='actualfile',
            name='remark',
            field=models.TextField(default=''),
        ),
    ]
