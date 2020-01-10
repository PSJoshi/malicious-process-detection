#!/usr/bin/env python

import psutil
import utils
import logging
import sys

# setup logging
logging.basicConfig(stream=sys.stdout,level=logging.INFO)
logger = logging.getLogger('ngram')

def check_process_status(p_name):
    '''
        Check if p_name process is amongest running process.
    '''
    for proc in psutil.process_iter():
        try:
            process_name = proc.name()
            # exact match 
            #if process_name.lower() == p_name.lower():
            # approximate match
            if p_name.lower() in process_name.lower():
                return True
                break 
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return False

def find_process_by_name(p_name):
    ''' 
        Find all processes with similar names(p_name)
    '''
    process_list = list()
    # iterate through all the processes
    for proc in psutil.process_iter():
        try:
            p_info = proc.as_dict(attrs = ['pid', 'name', 'create_time'])
            if p_name.lower() in p_info['name'].lower():
                process_list.append(p_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return process_list

def find_process_parent_info(p_name):
    '''
        Find process parent
    '''
    for proc in psutil.process_iter():
        try:
            # approximate match
            process_name = proc.name()
            if p_name.lower() in process_name:
                #process_name = proc.name()
                process_status = proc.status()
                parent_info = proc.parent()
                if parent_info:
                    process_parent_name, process_parent_pid = parent_info.name(),parent_info.pid

                    return process_name, process_status, process_parent_name, process_parent_pid

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    

if __name__ == "__main__":

    #print find_process_parent_info('firefox')
    #print find_process_by_name('firefox')
    #print check_process_status('firefox')

    # get the process names
    critical_process_list = list()
    for proc in psutil.process_iter():
        p_name = proc.name()
        critical_process_list.append(p_name)

    # loop through the list and print
    #for entry in critical_process_list:
    #    print entry

    # find out list of critical linux process ( See CIS benchmarks, NIST guides)
    for entry in critical_process_list:
        for proc in psutil.process_iter():
            p_name = proc.name()
            process_distance = utils.edit_distance(p_name.lower(),entry)
            if process_distance<5:
                print entry,p_name,process_distance
            
    
 
