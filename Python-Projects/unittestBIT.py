import unittest
from myutils import myutilities

class TestStrings(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_one_word(self):
        word = 'duck'
        res = myutilities.mywordcap(word)
        self.assertEqual(res, 'Duck')
        self.assertTrue(res == 'Duck')
        self.assertFalse(res == 'Duck')
        
    def test_more_words(self):
        words = 'ducks are awesome and cool'
        res = myutilities.mywordcap(words)
        self.assertEqual(res, 'Ducks Are Awesome and cool')
        
if __name__ == '__main__':
    unittest.main()

