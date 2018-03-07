# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 12:27:05 2018

@author: raecr
"""
import os
import re

def gettestlist():
    exelist = []
    if os.path.exists('../system_tests') == True:
        filelist = os.listdir('../system_tests')
        exepattern = re.compile('.*\Wexe')
        
        print('Collect all .exes...')
        for f in filelist:
            m = re.match(exepattern, f)
            if m != None:
                exelist.append(f)
                
    return exelist