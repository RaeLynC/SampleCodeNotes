# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 04:32:38 2018

@author: raecr
"""

class baseC():
    
    count = 0
    
    def __init__(self, n, d):
        self.__name = "**" + n + "**"
        self.index = -1
        self.__data = list(d)
        baseC.count += 1
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, n):
        self.__name = n
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, d):
        self.__data = list(d)
        
    @classmethod
    def printcount_class(cls):
        print(cls.count)
        
    @staticmethod
    def printcount_static():
        print('cant access private stuff!')
        
    def __eq__(self, baseobj):
        return ((self.__name.lower() == baseobj.name.lower()) \
            and (self.__data == baseobj.__data))
    
    def __ne__(self, baseobj):
        return (self.__name.lower() != baseobj.name.lower()) \
            and (self.__data != baseobj.__data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if (self.index == len(self.__data)):
            self.index = -1
            raise StopIteration
        return self.__data[self.index]
    
class derC(baseC):
    
    def __init__(self, n, d, x):
        super().__init__(n, d)
        self.x = x
        
    
if __name__ == '__main__':
    mylist = [2, 4, 6, 8]
    
    x = baseC('rae', mylist)
    y = baseC('rylee', [1, 3, 5, 7])
    z = baseC('RAE', [2, 4, 6, 8])
    
    print(x.name)
    print(x.data)
    baseC.printcount_class()
    baseC.printcount_static()
    if x == y:
        print('x == y')
    if x == z:
        print('x == z')
        
    for i in x:
        print(i)
        
    print((x!=y), " ", (x!=z))
    
    newlist = [1, 1, 1, 1, 1, 1, 1]
    x.data = newlist
    print('x.data', x.data)
    newlist[3] = 7
    print('x.data', x.data)
    x.data = newlist
    print('x.data', x.data)
    
    xder = derC('josh', [4,5,6,7], -5)
    print(xder.name, " ", xder.data, " ", xder.x)
    
    for i in xder:
        print(i)
        
    print('xder issubclass(baseC) - ', issubclass(type(xder), baseC))
    print('xder isinstance(baseC) - ', isinstance(xder, baseC))
    
    
    
    
    
    
    