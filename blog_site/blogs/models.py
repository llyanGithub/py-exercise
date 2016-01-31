# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    time = models.CharField(max_length=20)
    auth = models.CharField(max_length=20)
    path = models.CharField(max_length=200)

    def __str__(self):
        return self.title
