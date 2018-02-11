# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
class DeviceList(models.Model):
    ServerType = models.CharField(verbose_name='设备类型', max_length=20)

    def __str__(self):
        return self.ServerType.encode('utf-8')


class ServerList(models.Model):
    Supplier = models.CharField(verbose_name='供应商', max_length=8)
    Model = models.CharField(verbose_name='服务器型号', max_length=20)
    SN = models.CharField(max_length=20)
    PN = models.CharField(max_length=20, blank=True)
    Location = models.CharField(verbose_name='机柜位置', max_length=10, blank=True)
    Management_ip = models.GenericIPAddressField(verbose_name='管理口IP', max_length=16, default='192.168.0.120')
    Hostname = models.CharField(verbose_name='计算机名', max_length=20)
    IpAddr1 = models.GenericIPAddressField(max_length=16)
    IpAddr2 = models.GenericIPAddressField(max_length=16, null=True, blank=True)
    CpuType = models.CharField(verbose_name='CPU 型号', max_length=40)
    CpuPhysicsCore = models.IntegerField(verbose_name='CPU 物理核数', default='1')
    CpuLogicCore = models.IntegerField(verbose_name='CPU 逻辑核数', default='1')
    Memory = models.IntegerField(verbose_name='内存大小', default='2')
    HDD = models.IntegerField(verbose_name='磁盘大小', default='50')
    RAID = models.IntegerField(verbose_name='RAID类型', null=True, blank=True)
    Os = models.CharField(verbose_name='操作系统类型', max_length=16, blank=True)
    OsVersion = models.CharField(verbose_name='系统版本', max_length=40, blank=True)
    AddDate = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    ModDate = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    ServerType_id = models.ForeignKey(DeviceList)

    def __str__(self):
        return self.Hostname.encode('utf-8')
