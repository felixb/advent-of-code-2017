#! /usr/bin/env python3

import unittest
from extra import run

class MyTest(unittest.TestCase):
    def test_1212(self):
        self.assertEqual(run('1212'), '6')

    def test_1221(self):
        self.assertEqual(run('1221'), '0')

    def test_123425(self):
        self.assertEqual(run('123425'), '4')

    def test_123123(self):
        self.assertEqual(run('123123'), '12')

    def test_12131415(self):
        self.assertEqual(run('12131415'), '4')

if __name__ == '__main__':
    unittest.main()