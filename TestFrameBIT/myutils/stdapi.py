# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 12:53:05 2018

@author: raecr
"""

from collections import defaultdict
from collections import Counter
from collections import OrderedDict
import itertools

def dict_defaults():
    print('Testing default dictionary APIs')
    mylist = [0, 2, 4, 6]
    mytuple = ('rae', 'rylee', 'josh', 'brian')
    
    mydict = dict(zip(mylist, mytuple))
    print(mydict)
    
    print(mydict.get(0, 'def'))
    print(mydict.get(9, 'def'))
    
    mydefdict = defaultdict(lambda : 'def')
    for word in ['hi', 'yellow', 'strap']:
        mydefdict[word] = 7
    print(mydefdict.items())
    print(mydefdict['hi'], mydefdict['rae'])
    print(mydefdict.items())
    
def CounterAPI():
    print('Testing collections.counter for dict')
    mylist = [1, 2, 3, 4, 3, 2, 1]
    mytuple = (1, 1, 2, 3, 4, 5, 6, 3, 2, 1)
    
    counta = Counter(mylist)
    print(counta.items())
    countb = Counter(mytuple)
    print(countb.items())
    
    print('2 most common in counta: ', counta.most_common(2))
    diff = countb - counta
    print('countb - counta', diff)
    
def OrderedDictAPI():
    mylist = [1, 2, 3, 4, 3, 2, 1]
    mytuple = (1, 6, 2, 3, 4, 5, 1, 3, 2, 1)
    
    mydict = OrderedDict(zip(mytuple, mylist))
    print(mydict)
    mydict[7] = 4
    print(mydict)
    
    print('versus')
    mydict = dict(zip(mytuple, mylist))
    print(mydict)
    mydict[7] = 4
    print(mydict)   
    
def itertoolsAPI():
    print('itertoolsAPI')
    print('\tcycle:')
    counter = 0
    for item in itertools.cycle([1, 2, 3]):
        counter += 1
        if counter == 30:
            break
        print(item, end='')
    print('\tend-cycle')
    
    for i, item in enumerate(itertools.accumulate([2, 4, 6, 8])):
        print(i, ' ', item)
        
    for i, item in enumerate(range(0,3)):
        print(i, ' ', item)
        
    
fctlist = [dict_defaults, CounterAPI, OrderedDictAPI, itertoolsAPI]