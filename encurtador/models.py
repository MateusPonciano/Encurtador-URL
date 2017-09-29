# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Url(models.Model):
    url_name = models.URLField(unique=True)
    code = models.IntegerField(default=0, unique=True)

'''
    def encurtar(url):
        code = transformar id base 10 para 36 (numpy)
        localhost:8000/code
'''
