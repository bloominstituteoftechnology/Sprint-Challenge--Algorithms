import unittest
import random
from count_th import *

cache = {'th':0}

class Test(unittest.TestCase):

    def setUp(self):
        self.word = ""

    def test_count_th_empty(self):
        cache = {'th':0}
        self.word = ""
        count = count_th(self.word)
        self.assertEqual(0, count)

    def test_count_th_single(self):
        cache = {'th':0}
        self.word = "abcthxyz"
        count = count_th(self.word)
        self.assertEqual(1, count)
    
    def test_count_th_multiple(self):
        cache = {'th':0}
        self.word = "abcthefthghith"
        count = count_th(self.word)
        self.assertEqual(3, count)

    def test_count_backwards(self):
        cache = {'th':0}
        self.word = "thhtthht"
        count = count_th(self.word)
        self.assertEqual(2, count)

    def test_count_th_mixedcase(self):
        cache = {'th':0}
        self.word = "THtHThth"
        count = count_th(self.word)
        self.assertEqual(1, count)

    
if __name__ == '__main__':
    unittest.main()
