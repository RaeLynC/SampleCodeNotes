import multiprocessing
import os

def myfct(what = 'def'):
    whoami(what)
    
def whoami(what):
    print('Proc {} : {}'.format(os.getpid(), what))

if __name__ == '__main__':
    whoami('I am main!')
    
    for i in range(3):
        myfct()
        p = multiprocessing.Process(target = myfct, args = ('child!',))
        p.start()
