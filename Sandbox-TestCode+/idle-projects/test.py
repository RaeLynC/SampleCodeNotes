#!/usr/bin/python

mystr = "hello"
mylist = list(mystr)

print(mylist)

def enliven(c):
    return c.upper() + '!'

def printletters(word, fct):
    for c in word:
        print(fct(c))

        
printletters(mystr, enliven)
printletters(mylist, lambda c: c.upper() + '!')

