# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-27 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flexfeed', '0005_auto_20171027_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='site',
            field=models.CharField(blank=True, choices=[('IG', 'Instagram'), ('TWT', 'Twitter'), ('FB', 'Facebook')], default='FB', help_text='Choose the site this post is on', max_length=3),
        ),
    ]
