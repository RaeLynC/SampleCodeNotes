# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 05:27:11 2018

@author: raecr
"""

class baseC:
    count = 0
    
    def __init__(self, name):
        self.__name = name
        baseC.count += 1
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, n):
        self.__name = n
        
    @classmethod
    def printcount(cls):
        print('baseC: {}'.format(cls.count))
     
# Iterable class!
class derivedC(baseC):
    
    def __init__(self, name, data):
         super().__init__(name)
         self.index = -1
         self.data = data
         
    # special method: compare names, ignoring case!
    def __eq__(self, word):
        return (self.name.lower() == word.lower())

    def printResults(self):
        print('No results yet')
        
    def __iter__(self):
        'Return self as an iterator object'
        return self
    
    def __next__(self):
        self.index += 1
        if self.index == len(self.data):
            self.index = -1
            raise StopIteration
        return self.data[self.index]
        
        
        
        
        
        
        
        
        
        