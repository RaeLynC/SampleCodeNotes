# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 11:51:12 2018

@author: raecr
"""

class Cbook:
    def __init__(self, title, author):
        self.info = (title, author)
        
    def __eq__(self, other):
        if (self.info[0].upper() == other.info[0].upper()) \
            and (self.info[1].upper() == other.info[1].upper()):
            return True
        return False
        
    def printme(self):
        print(self.info[0].upper(), '\tby', self.info[1])
        
    def __str__(self):
        #return '{} : {}'.format(self.info[0], self.info[1])
        return '{} : {}'.format(*self.info)
