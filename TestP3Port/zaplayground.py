# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 05:34:36 2018

@author: raecr
"""
spam = "global-spam"

def dec_it(f):
    def new_fct(*args):
        print('Fct:', f.__name__)
        print('w/args', args)
        newargs = []
        for i in args:
            newargs.append(i*i)
        print(newargs)
        args = tuple(newargs)
        res = f(*args)
        return res
    return new_fct
  
@dec_it
def mygen(start, stop, step=1):
    index = start
    while (index <= stop):
        yield index
        index += step
        
def myfct():
    spam = "green"
    def inner_fct(): 
        nonlocal spam
        spam = 'yellow'
        print(spam)
    inner_fct()
    print(spam)
        

if __name__ == '__main__':
    
    import sys
    
    for i,j in enumerate(sys.path):
        print(i, j)

