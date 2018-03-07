# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 10:30:23 2018

@author: raecr
"""

localvar = 8
print(__name__)
if __name__ == "__main__":
    print('****I am main!')
else:
    print('!main: {}'.format(__name__))
    
def myfct(x, str):
    print(localvar)
    print('myfct: {0} {1}'.format(x, str))
    
def myfct1(x):
    print(localvar)
    print('myfct: {0}'.format(x))