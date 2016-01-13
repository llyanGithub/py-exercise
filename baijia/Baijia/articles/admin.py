# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from .models import Author, articles

admin.site.register(Author)
admin.site.register(articles)
