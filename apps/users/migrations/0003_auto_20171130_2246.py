# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-30 22:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_banner_emailcode'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': '\u8f6e\u64ad\u56fe', 'verbose_name_plural': '\u8f6e\u64ad\u56fe'},
        ),
        migrations.AlterModelOptions(
            name='emailcode',
            options={'verbose_name': '\u90ae\u7bb1\u9a8c\u8bc1\u7801', 'verbose_name_plural': '\u90ae\u7bb1\u9a8c\u8bc1\u7801'},
        ),
        migrations.AlterModelOptions(
            name='userwrapper',
            options={'verbose_name': '\u7528\u6237\u4fe1\u606f', 'verbose_name_plural': '\u7528\u6237\u4fe1\u606f'},
        ),
    ]
