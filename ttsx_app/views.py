# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import *
from django.template import loader, RequestContext
from  models import *

# Create your views here.
def index(request):
    ServerList1 = ServerList.objects.all()[:3]
    return render(request, 'index.html', locals())

def base(request):
    return render(request, 'base.html')

def logins(request):
    if request.method ==
    return render(request, 'login.html', locals())