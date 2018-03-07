# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 05:29:32 2018

@author: raecr
"""

from classBIT import classBITC

if __name__ == '__main__':
    print('STD Library API testing')
    
    mybase = classBITC.baseC('base class')
    print(mybase.name)
    mybase.name = 'rae'
    print(mybase.name)
    
    # Note: 2nd arg tests derived class iterable-ness
    myderived = classBITC.derivedC('derived class', [2,4, 6, 8])
    print(myderived.name)
    myderived.name = 'Josh'
    print(myderived.name)
    myderived.printResults()
    
    if isinstance(myderived, classBITC.baseC):
        print('isinstance(myderived, classBITC.baseC)')
    else:
        print('NOT isinstance(myderived, classBITC.baseC)')
        
    if isinstance(myderived, classBITC.derivedC):
        print('isinstance(myderived, classBITC.stdbitC)')
    else:
        print('NOT isinstance(myderived, classBITC.stdbitC)')
        
    if issubclass(type(myderived), classBITC.baseC):
        print('issubclass(myderived, classBITC.baseC)')
    else:
        print('NOT issubclass(myderived, classBITC.baseC)')
        
    # Test class method
    classBITC.baseC.printcount()
    
    # Test special ops
    print(myderived == 'josh') # true
    print(myderived == 'rae') # false
    
    #iterate the derived class!
    for i in myderived:
        print(i, end=' ')
    for i in myderived:
        print(i, end=' ')
        
    #built-in fcts take iterable types
    mylist = list(myderived)
    print(mylist)
      