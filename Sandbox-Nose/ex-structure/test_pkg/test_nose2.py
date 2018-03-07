from nose import with_setup
from myutils import myutilities as myutil
 
def setup_module(module):
    print ("") # this is to get a newline after the dots
    print ("n2 - setup_module")
 
def teardown_module(module):
    print ("n2 - teardown_module")
 
def fct_setup():
    print ("n2 - fct-setup")
 
def fct_teardown():
    print ("n2 - fct-teardown")
 
# Test generatior functionality
@with_setup(fct_setup, fct_teardown)
def test_evens():
    for i in range(0, 5):
        yield check_even, i, i*3

def check_even(n, nn):
    assert n % 2 == 0 or nn % 2 == 0
