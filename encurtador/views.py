# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponse
from .forms import UrlForm
# Create your views here.

class indexView(FormView):
    model = UrlForm
