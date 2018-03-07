# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 11:07:30 2018

@author: raecr
"""

import os
import pickle
from librarypkg import *

if __name__ == '__main__':
    
      
    mylist = [4, 5, 6, 7]
    mynames = ['rae', 'rylee', 'josh']
    a = Cbook('dog', 'Rylee Coates')
    b = Cbook('cow', 'Joshua Coates')
    lib = library.Clibrary('Goffstown')
    lib.addBook(a)
    lib.addBook(b)

    with open('junk.txt', 'wb') as f:
        pickle.dump(mylist, f)
        pickle.dump(mynames, f)
        pickle.dump(a, f)
        pickle.dump(b, f)
        pickle.dump(lib, f)

    with open('junk.txt', 'rb') as f:
        while True:
            try:
                o = pickle.load(f)
            except EOFError:
                break
            else:
                if not isinstance(o, library.Clibrary):
                    print(o)
                else:
                    print(o.name)
                    for i in o:
                        print('\t',i)