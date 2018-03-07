# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 10:05:23 2018

@author: raecr
"""

class baseC:
    count = 0
    
    def __init__(self, name, d):
        baseC.count += 1
        self.__name = name
        self.data = d
        self.index = -1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index == len(self.data):
            self.index = -1
            raise StopIteration
        return self.data[self.index]
        
    def __eq__(self, othername):
        if (self.__name.upper() == othername.upper()):
            return True
        return False
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, n):
        self.__name = n
        
    @classmethod
    def printcount(cls):
        print('baseC::count - {}'.format(cls.count))
        
    @staticmethod
    def mystaticmethod():
        print('just an associated fct')