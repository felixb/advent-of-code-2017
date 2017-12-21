#! /usr/bin/env python3

import unittest
from main import run

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(run("5 1 9 5\n7 5 3\n2 4 6 8"), '18')

if __name__ == '__main__':
    unittest.main()