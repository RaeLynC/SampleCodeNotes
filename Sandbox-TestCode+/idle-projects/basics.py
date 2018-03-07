#j!/usr/bin/python


animal = 'cat'

def dec_it(fct):
    def newfct(x):
        print ("Fct:", fct.__name__)
        print ("arg", x)
        result = fct(x)
        print result
        return result
    return newfct

@dec_it
def myfct(x):
    global animal

    print animal
    animal = 'dog'
    print("myfct: ", x)
    return 7, 8

myfct(9)
print animal
