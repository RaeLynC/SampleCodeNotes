# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 17:56:41 2018

@author: raecr
"""
import subprocess

def syscallBIT():
    print('Try executing a test!')

    process = subprocess.Popen('echo hi', shell=True, stdout=subprocess.PIPE)
    process.wait()
    print(process.stdout.read())
    
    # needs to be compiled in DOS!
    print('try this')
    process = subprocess.Popen('hw.exe', shell=True, stdout=subprocess.PIPE)
    process.wait()
    print(process.returncode) #test failed, not compiled on DOS!
    
    ret = subprocess.getstatusoutput('echo hi')
    print(ret)
    ret = subprocess.getstatusoutput('./hw1.exe')
    print(ret)
    