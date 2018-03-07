# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 10:52:10 2018

@author: raecr
"""

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