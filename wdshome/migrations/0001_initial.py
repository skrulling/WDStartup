# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 13:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Annonser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittel', models.CharField(max_length=150)),
                ('dato', models.DateTimeField(auto_now=True)),
                ('kvalik', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=100)),
                ('stillinger', models.IntegerField()),
                ('info', models.TextField(max_length=1000)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
