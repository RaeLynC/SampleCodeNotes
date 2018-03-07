# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 12:02:39 2018

@author: raecr
"""

# Build functionality to use with unittestBIT.py
def mywordcap(s):
    from string import capwords
    return capwords(s)

def getuserint(start, end):
    intval = -1
    while intval < start or intval > end:
        intval = input('Enter option[{}-{}], q-quit: '.format(start, end))
        try:
            if intval == 'q':
                break
            intval = int(intval)
        except ValueError:
            print('Invalid value, retry...')
            intval = -1
    return intval
