from myutils import myutilities as myutil
from nose.plugins.attrib import attr
from nose.tools import assert_equals

def test_numbers_3_4():
    assert myutil.multiply(3,4) == 12 
 
def test_strings_a_3():
    assert myutil.multiply('a',3) == 'aaa'

@attr(tags='tools, slow')
def test_nosetools():
    print('here')
    assert_equals('Rae', 'R'+'a'+'e')
