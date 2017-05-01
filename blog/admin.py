# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post,Article
admin.site.register(Post)
admin.site.register(Article)

# Register your models here.
