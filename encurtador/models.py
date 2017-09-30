# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Url(models.Model):
    url_name = models.URLField(unique=True)
    code = models.CharField(default='0', unique=True, max_length=100)
