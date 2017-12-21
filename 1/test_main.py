#! /usr/bin/env python3

import unittest
from main import run

class MyTest(unittest.TestCase):
    def test_1122(self):
        self.assertEqual(run('1122'), '3')

    def test_1111(self):
        self.assertEqual(run('1111'), '4')

    def test_1234(self):
        self.assertEqual(run('1234'), '0')

    def test_91212129(self):
        self.assertEqual(run('91212129'), '9')

if __name__ == '__main__':
    unittest.main()