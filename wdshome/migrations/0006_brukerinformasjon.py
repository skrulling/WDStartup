# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 19:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wdshome', '0005_auto_20160422_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brukerinformasjon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('erfaring', models.CharField(max_length=200)),
                ('hjemmeside', models.URLField()),
                ('om_meg', models.TextField(max_length=1000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]