# -*- coding: utf-8 -*-

import copy
    
if __name__ == '__main__':
    
    # single-dim array!!
    print('shallow copy')
    mylist = [3, 4, 5]
    b = mylist
    print(mylist, "\t**", b)
    mylist[2] = -5
    print (mylist, "\t**",b)
    
    print('deep copy')
    mylist = [3, 4, 5]
    b = list(mylist)
    print(mylist, "\t**", b)
    mylist[2] = -5
    print (mylist,"\t**", b)
    
    
    # multi-dim!!
    print('shallow copy')
    mylist = [[3, 4, 5], [11, 12, 13]]
    b = mylist
    print(mylist, "\t**", b)
    mylist[0][2] = -5
    print (mylist, "\t**",b)
    
    print('deep copy')
    mylist = [[3, 4, 5], [11, 12, 13]]
    b = copy.deepcopy(mylist)
    print(mylist, "\t**", b)
    mylist[0][2] = -5
    print (mylist,"\t**", b)

    
    



    