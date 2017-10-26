# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flexfeed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.URLField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='stock',
            name='value',
            field=models.DecimalField(decimal_places=2, help_text='The value of the stock.', max_digits=5),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(help_text='Enter your first name', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(help_text='Enter your last name', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Enter your username (max 15 characters): ', max_length=25),
        ),
    ]