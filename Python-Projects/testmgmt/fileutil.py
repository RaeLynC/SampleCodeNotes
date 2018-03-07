# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 12:26:54 2018

@author: raecr
"""
import time

def getdateddirname():
    name = time.ctime(time.time())
    name= name.replace(':','')
    name = 'Bld-' + name.replace(' ', '-')
    return name

def getdatedfilename():
    name = time.ctime(time.time())
    name = name.replace(' ', '-') + '.txt'
    return name