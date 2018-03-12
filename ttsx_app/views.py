# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import *
from django.template import loader, RequestContext
from  models import *
from django.core import exceptions
from ttsx_app.forms import add_serverform

# Create your views here.
def index(request):
    ServerList1 = ServerList.objects.all()[:3]
    return render(request, 'index.html', locals())

def base(request):
    return render(request, 'base.html')

# def logins(request):
#     if request.method == POST:
#
#     return render(request, 'login.html', locals())

def add_server(request):
    add_servers = add_serverform(request.POST)
    if add_servers.is_valid():
        add_servers.save()
        # return render(request, 'register.html', locals())
        return HttpResponse("添加成功")
    else:
        add_servers = add_serverform()
    return render(request, 'register.html', locals())