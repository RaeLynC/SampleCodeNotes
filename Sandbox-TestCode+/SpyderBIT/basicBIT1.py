# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 12:22:04 2018

@author: raecr
"""
#closure fct
def capturestr(s):
    def innerfct():
        print('helloagain {}'.format(s))
    return innerfct

# generator
def myranger():
    count = 0
    while (count < 10):
        yield count
        count += 2
        
# lambda
def modifyval(x, fct):
    return fct(x)

if __name__ == '__main__':
    print('Executing fct types')
    
    print('closure fct')
    f = capturestr('Duck')
    f()
    f()
    
    print('generator fct')
    for i in myranger():
        print(i)
        
    print('lambda!')
    for i in myranger():
        print(modifyval(i, lambda x: x*3))
    
    
    print('zip/range/comprehensions (+generator comprehension)')
    mylist = [0, 2, 4, 6, 8]
    myset = {1, 3, 5, 7, 9}
    res = zip(mylist, myset)
    print(list(res))
    print(dict(res)) # will be empty!
    
    for i in range(6,3,-1):
        print(i)
        
    mylist = [str(i*10)+'hi' for i in range(1,10,2) if i < 9]
    print(mylist)
    
    mydict = {i:str(i)+'hi' for i in range(1,10,2) if i < 9}
    print(mydict)
    
    mygen = (i+'hello' for i in mylist)
    for i in mygen:
        print(i)
    