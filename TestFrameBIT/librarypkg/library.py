# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 11:50:53 2018

@author: raecr
"""
class Clibrary:
    numlibraries = 0
    
    def __init__(self, name):
        self.index = -1
        self.__name = name
        self.booklist = []
        Clibrary.numlibraries += 1
        
    @property
    def name(self):
        return self.__name
    
    def addBook(self, book):
        if book not in self.booklist:
            self.booklist.append(book)
    
    @classmethod
    def getbookcount(cls):
        return cls.numlibraries
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if (self.index == len(self.booklist)):
            self.index = -1
            raise StopIteration
        return(self.booklist[self.index])
