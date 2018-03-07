#!/usr/bin/python
import sys
from Sources import single, double
from Sources.patron import Patron

print 'Library App'

def editwords(alist, fct):
    for i in alist:
        print fct(i)


wordlist = []
wordlist.append('rae')
wordlist.append('rylee')
wordlist.append('josh')

print wordlist
editwords(wordlist, lambda word: word.upper()+'!!!')

print("argv: ", sys.argv)
print sys.argv[1]
print "sys search path"
for num, i in enumerate(sys.path, 1):
    print num, i 

print "single random names:"
for i in range(0, 7):
    print '\t' + single.get_random_name()

print "double random names:"
print double.get_random_name()

someone = Patron("brian coates")
print someone.name
