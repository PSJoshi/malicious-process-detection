#!/usr/bin/env python
import os
import psutil
import time
import sys

process_info = list()
 
for proc in psutil.process_iter():
    try:
        pinfo = proc.as_dict(attrs=['pid', 'name', 'username','cpu_percent','memory_percent','memory_info'])
        process_info.append([pinfo['name'], pinfo['cpu_percent'], pinfo['memory_percent'], pinfo['memory_info'].rss, pinfo['memory_info'].vms])
    except psutil.NoSuchProcess:
        pass

print process_info


