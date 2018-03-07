# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 11:51:34 2018

@author: raecr
"""

from librarypkg import *

if __name__ == '__main__':
    lib = Clibrary('Goffstown')
    
    print(lib.name)
    print(lib.getbookcount())
    
    booka = Cbook("cows", "Josh Coates")
    bookb = Cbook("dogs", "Rylee Coates")
    bookc = Cbook("cows!", "Josh Coates")
    
    lib.addBook(booka)
    lib.addBook(bookb)
    if booka == bookc:
        print('Equal')
    else:
        print('not equal!')
    lib.addBook(bookc)
    
    for i, j in enumerate(lib):
        print(i, end = ': ')
        j.printme()