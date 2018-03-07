# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 12:25:23 2018

@author: raecr
"""
from testmgmt import fileutil, testutil
import os
import shutil

print('Nightly test run:')
testlist = testutil.gettestlist()
print(testlist)

#execute the tests, printing output in date-time-results files
if os.path.exists('../results') == False:
    os.mkdir('../results')
elif len(os.listdir('../results')) > 2:
    print('Delete results dir, every 3x')
        
    #shutil.rmtree('../results', ignore_errors=True)
    shutil.rmtree('../results')
    if os.path.exists('../results') == True:
        reslist = os.listdir('../results')
        print(reslist)
        print('it still exists')
    else:
        os.mkdir('../results')

    
# Manage today's build results
resultdir = '../results/' + fileutil.getdateddirname()
print(resultdir)
os.mkdir(resultdir)
    
prior = testfilename = ''
for t in testlist:
    while prior == testfilename:
        testfilename = resultdir + '/' + fileutil.getdatedfilename()
        #print('still getting unique name...')
    print(testfilename)
    try:
        f = open(testfilename, 'x')
        f.write(t)
        f.close()
        prior = testfilename
    except FileExistsError:
        print('File {} failed to open\n'.format(testfilename))
        

    






print('done!')