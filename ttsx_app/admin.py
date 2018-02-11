# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
class ServerListAdminInLine(admin.TabularInline):
    model = ServerList
    extra = 2

class ServerListAdmin(admin.ModelAdmin):
    list_display = ['id', 'Hostname', 'IpAddr1', 'CpuLogicCore', 'Memory', 'HDD', 'AddDate', 'ModDate']
    list_filter = ['Hostname']
    search_fields = ['Hostname', 'IpAddr']
    readonly_fields = ['AddDate', 'ModDate']
    # inlines = [ServerListAdminInLine]


admin.site.register(DeviceList)
admin.site.register(ServerList, ServerListAdmin)
