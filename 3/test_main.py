#! /usr/bin/env python3

import unittest
from main import run_1, run_2

class Test(unittest.TestCase):
    def test_1_1(self):
        self.assertEqual(run_1("1"), 0)

    def test_1_12(self):
        self.assertEqual(run_1("12"), 3)

    def test_1_23(self):
        self.assertEqual(run_1("23"), 2)

    def test_1_1024(self):
        self.assertEqual(run_1("1024"), 31)

if __name__ == '__main__':
    unittest.main()