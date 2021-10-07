"""The test suite for keylang.py

Author: Jacob Kerr, 2021
"""
import sys

sys.path.insert(1, ".")

import unittest
from gachapy import *


def test_lang(test: unittest.TestCase, program: str, rarity: float, expected: float):
    """Asserts that the program parses and interprets to the expected result
    
    Paramters
    ---------
    test : unittest.TestCase
        the test case to run the test on
    program : str
        the program string to parse and interpret
    rarity : float
        the rarity to insert into the equation
    expected : float
        the expected value of the program"""
    ast = parse(program)
    result = interpret(ast, rarity)
    test.assertEqual(result,expected)


class TestKeyLang(unittest.TestCase):
    """Test suite for keylang.py"""

    def test_1_plus_1(self):
        test_lang(self,"1 + 1",0,2)

    def test_2_times_2(self):
        test_lang(self,"2 * 2", 0, 4)

    def test_2_pow_2(self):
        test_lang(self,"2 ^ 2", 0, 4)

    def test_1_plus_2_times_2(self):
        test_lang(self,"1 + 2 * 2", 0, 5)
    
    def test_2_times_2_plus_1(self):
        test_lang(self,"2 * ( 1 + 2 )", 0, 6)

    def test_1_plus_rarity(self):
        test_lang(self, "1 + R", 1, 2)