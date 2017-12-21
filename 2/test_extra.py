#! /usr/bin/env python3

import unittest
from extra import run

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(run("5 9 2 8\n9 4 7 3\n3 8 6 5"), '9')

if __name__ == '__main__':
    unittest.main()