#! /usr/bin/python
#--coding:utf8--
from subprocess import PIPE,Popen
import os,sys

def CPU():
    with open('/proc/cpuinfo') as cpu:
        n=0
        for i in cpu:
            if i.startswith('process'):
                n += 1
            if i.startswith('model name'):
                cpu_model = i.split(':')[1]

if __name__ = '__main__':
    cpuinfo = CPU()
    print cpuinfo
