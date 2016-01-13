# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='articles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_title', models.CharField(max_length=100)),
                ('article_abstract', models.CharField(max_length=500)),
                ('article_href', models.CharField(max_length=100)),
                ('pic_href', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('auth_name', models.CharField(max_length=20)),
                ('classification', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='auth_id',
            field=models.ForeignKey(to='articles.Author'),
        ),
    ]
