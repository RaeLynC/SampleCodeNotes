# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 13:19:41 2018

@author: raecr
"""
counter = 0

def menu(*args, **kwargs):
    'my first fct'
    global counter
    print(counter)
    counter += 1
    if len(args) > 0:
        print(args)
    if len(kwargs) > 0:
        print(kwargs)
        
# closure
def myclosurefct(strx):
    def innerfct():
        return 'Hello {}'.format(strx)
    return innerfct

# lambda
def modifylist(alist, fct):
    newlist = []
    for i in alist:
        newlist.append(fct(i))
    print('Results: ', newlist)
    return newlist

# Generator
def reverse(data):
    for i in range(len(data)-1, -1, -1):
        yield data[i]
    
if __name__ == '__main__':
    menu('white', 'steak', 'cake')
    menu('red', 'chicken', dessert='icecream')
    
    print('Test closure:')
    f = myclosurefct('rylee')
    print(f())
    
    print('Test Lambda:')
    mylist = [2, 4, 6, 8]
    a = modifylist(mylist, lambda i : i * i)
    print('A: ', a)
    b = modifylist(a, lambda i : i * i)
    print('A: ', a)
    print('B: ', b)
    
    print('Test Generator fct:')
    mylist = [2, 3, 5, 7, 8, 1]
    for i in reverse(mylist):
        print(i)
    
    
    
    

    
