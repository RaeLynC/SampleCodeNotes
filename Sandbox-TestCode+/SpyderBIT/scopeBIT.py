spam = 'global spam'
def scope_test():
    def do_local():
        nonlocal spam
        spam = "local spam"

    def do_global():
        global spam
        spam = "global changed"
        
    spam = "test spam"
    
    do_local()
    print("After local assignment:", spam)

    do_global()
    print("After global assignment:", spam)

if __name__ == '__main__':
    scope_test()
    print("In global scope:", spam)