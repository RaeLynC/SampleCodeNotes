import os
import subprocess

def killprocbyname(s):
    import psutil
    
    # 2. if junk is running, kill it
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == s:
            print('it\'s running!')
            proc.kill()
            
def catfiles(filelist):
    with open('catfile.txt', 'w') as outfile:
        for i in filelist:
            with open(i, 'r') as infile:
                for line in infile:
                    outfile.write(line)
    with open('catfile.txt', 'r') as catfile:
        for line in catfile:
            print(line)
            
def compare_files(f1, f2):
    cmd = str('fc {} {}'.format(f1, f2))
    ret = subprocess.getoutput(cmd)
    if (ret.endswith('no differences encountered\n')):
        print('matching files!!!!')
        return True
    return False
    

if __name__ == '__main__':
    textfiles = []
    print(os.getcwd())

    # 1. List all .txt files
    ret = os.listdir()
    for i in ret:
        #check i ends with '.txt'
        if i.endswith('.txt'):
            textfiles.append(i)
    print(textfiles)
    
    #ccompare files!
    print(compare_files(textfiles[0], textfiles[1]))
    
    killprocbyname('junk.exe')
    
    catfiles(textfiles)

        