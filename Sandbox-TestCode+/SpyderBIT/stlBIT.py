# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 10:43:44 2018

@author: raecr
"""
from myutil import myutilfcts, stdapi

numfcts = len(stdapi.fctlist)

#res = myutilfcts.getuserint(0, numfcts-1) 
#while res != 'q':

for i in range(0,numfcts):
    print (i)
    f = stdapi.fctlist[i]
    f()
   # res = myutilfcts.getuserint(0, numfcts-1)
