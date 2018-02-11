# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import *
from django.template import loader, RequestContext

# Create your views here.
def index(request):
    # tmp=loader.get_template('index.html')
    # return HttpResponse(tmp.render())
    return render(request, 'index.html')