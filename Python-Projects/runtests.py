# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 12:25:23 2018

@author: raecr
"""
from testmgmt import fileutil, testutil
import os
import re
import subprocess

if __name__ == '__main__':
    print('Nightly test run:')
    print(fileutil.getdatedfilename())
    testlist = testutil.gettestlist()
    print(testlist)

    #execute the tests, printing output in date-time-results files
    if os.path.exists('../results') == False:
        os.mkdir('../results')
    resultsdir = '../results/' + fileutil.getdateddirname()
    print(resultsdir)
    os.mkdir(resultsdir)
    print(os.listdir('../results'))

    print('Try executing a test! - return status only')
    ret = subprocess.call('../system_tests/hw.exe')
    print('ret: ')
    print(ret)
    if ret != 0:
        print('Test failed')
    else:
        print('Test succeeded')

    print('done!')
