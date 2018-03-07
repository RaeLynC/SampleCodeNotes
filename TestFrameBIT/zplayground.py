# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 16:39:42 2018

@author: raecr
"""
    
if __name__ == '__main__':

    mylist = list(range(0,100))
    newlist = []
    
    with open('file.txt', 'w') as outfile:
        for i in mylist:
            outfile.write(str(i)+'\n')
            
    with open('file.txt', 'r') as infile:
        newlist = infile.readlines()
        
    xlist = list(map(lambda s: int(s), newlist))
    print (xlist)
    
    ylist = any(x%2 == 0 for x in xlist)
    print(ylist)
    