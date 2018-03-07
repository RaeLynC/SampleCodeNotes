from myutils import myutilities as myutil
from nose import with_setup
from nose.plugins.attrib import attr
from nose.tools import assert_is_instance
from nose.tools import assert_not_is_instance
from nose.tools import assert_is
from nose.tools import assert_is_not
from nose.tools import assert_in
from nose.tools import assert_not_in
from nose.tools import assert_true
from nose.tools import assert_false
from nose.tools import assert_equals
from nose.tools import assert_not_equal
from nose.tools import raises
import time
from nose.tools import timed
from nose.tools import nottest

 
def setup_module(module):
    print ("") # newline after the dots
    print ("test_cls:setup_module")
 
def teardown_module(module):
    print ("test_cls:teardown_module")
 
@attr(ttype='tools')
class TestToolsBIT:
    mytuple = (1,2,3)
    mylist = []
 
    def setup(self):
        print ("TestToolsBIT::setup().. fct")
 
    def teardown(self):
        print ("TestToolsBIT::teardown().. fct")
 
    @classmethod
    def setup_class(cls):
        cls.mylist = ['rae', 'rylee', 'josh', 'brian']
        cls.mylistptr = cls.mylist
        cls.mytupleptr = cls.mytuple
        print ("TestToolsBIT()")
 
    @classmethod
    def teardown_class(cls):
        print ("TestToolsBIT()")

    @attr('undertest')
    def test_is_instance(self):
        assert_is_instance(TestToolsBIT.mylist, list)

    @attr('undertest')
    def test_not_is_instance(self):
        assert_not_is_instance(TestToolsBIT.mylist, tuple)

    # Items are the same item
    def test_is(self):
        assert_is(TestToolsBIT.mylist, TestToolsBIT.mylistptr)

    # Items are NOT the same item
    def test_is_not(self):
        assert_is_not(TestToolsBIT.mylist, TestToolsBIT.mytupleptr)
 
    def test_in(self):
        assert_in('rylee', TestToolsBIT.mylist)

    def test_notin(self):
        assert_not_in('scarlett', TestToolsBIT.mylist)

    def test_true(self):
        assert_true(TestToolsBIT.mytuple == (1,2,3))

    def test_false(self):
        assert_false(TestToolsBIT.mytuple == (2,2,2))

    def test_EQ(self):
        assert_equals(myutil.multiply(5,6), 30)

    def test_notEQ(self):
        assert_not_equal(myutil.multiply(5,6), 31)

    @raises(TypeError)
    def test_raises(self):
        raise TypeError("This test passes")

    @timed(.2)
    def test_timed(self):
        time.sleep(.1)

    @nottest
    def test_dontrunme(self):
        print('test_dontrunme!')
