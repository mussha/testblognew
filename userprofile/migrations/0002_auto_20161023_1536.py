# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-23 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='read',
            field=models.ManyToManyField(blank=True, null=True, to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='subs',
            field=models.ManyToManyField(blank=True, null=True, to='blog.Blog'),
        ),
    ]
