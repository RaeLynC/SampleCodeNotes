# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 10:05:37 2018

@author: raecr
"""

def myclosurefct(s):
    def innerfct():
        print('Hi!! {}'.format(s))
    return innerfct