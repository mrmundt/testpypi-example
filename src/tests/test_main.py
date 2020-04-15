"""
Test_main:
    Tests the printWords 
"""

import unittest
from src.tests.utils import category
from src.main.main import printWords, printTupleWords

class MyTestCase(unittest.TestCase):
    @category('normal', 'fun')
    def test_printWords(self):
        self.assertEqual(printWords(['hello']), ['hello'])
        
    @category('weird', 'boring')
    def test_printTupleWords(self):
        self.assertEqual(printTupleWords(('hello')), ('hello'))

