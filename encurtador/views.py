# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UrlForm
from django.views import View
from .models import Url
import numpy as np
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import redirect
from django.views.generic.list import ListView
# Create your views here.

class IndexView(FormView):
    form_class = UrlForm
    model = UrlForm
    fields = ['url_name']
    template_name = 'index.html'

class Encurtar(View):
    template_name = 'show_new_url.html'

    def post(self, request):
        form = UrlForm(request.POST)

        if form.is_valid():
            url_field = form.cleaned_data['url_name']
            url = Url.objects.create(url_name=url_field)
            url.code = np.base_repr(url.id, base=36)
            url.save()

        else:
            try:
                url = Url.objects.get(url_name=request.POST['url_name'])
            except ObjectDoesNotExist:
                print("Url Does Not Exist")

        return render(request, self.template_name, {'url_name': url.url_name, 'code': url.code, 'pk': url.id})

class LinkView(SingleObjectMixin, View):
    model = Url

    def get(self, request, code):
        short_code = request.GET.get('code')
        url = Url.objects.get(code=short_code)

        return redirect(url.url_name)

class ListUrls(ListView):
    model = Url
    template_name = 'list_url.html'
