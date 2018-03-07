from nose import with_setup
from myutils import myutilities as myutil
 
def setup_module(module):
    print ("") # this is to get a newline after the dots
    print ("setup_module before anything in this file")
 
def teardown_module(module):
    print ("teardown_module after everything in this file")
 
def fct_setup():
    print ("my_setup")
 
def fct_teardown():
    print ("my_teardown")
 
@with_setup(fct_setup, fct_teardown)
def test_numbers_3_4():
    print 'test_numbers_3_4  <============================ actual test code'
    assert myutil.multiply(3,4) == 12
 
@with_setup(fct_setup, fct_teardown)
def test_strings_a_3():
    print 'test_strings_a_3  <============================ actual test code'
    assert myutil.multiply('a',3) == 'aaa'
 
 
class TestUM:
 
    def setup(self):
        print ("TestUM:setup() before each test method")
 
    def teardown(self):
        print ("TestUM:teardown() after each test method")
 
    @classmethod
    def setup_class(cls):
        print ("setup_class() before any methods in this class")
 
    @classmethod
    def teardown_class(cls):
        print ("teardown_class() after any methods in this class")
 
    def test_numbers_5_6(self):
        print 'test_numbers_5_6()  <============================ actual test code'
        assert myutil.multiply(5,6) == 30
 
    def test_strings_b_2(self):
        print 'test_strings_b_2()  <============================ actual test code'
        assert myutil.multiply('b',2) == 'bb'

def test_strings_z_4():
    print 'test_strings_z_4  <============================ actual test code'
    assert myutil.multiply('z',4) == 'zzzz'
