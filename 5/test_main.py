#! /usr/bin/env python3

import unittest
from main import run_1, run_2


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(run_1("0\n3\n0\n1\n-3"), 5)
    def test_2(self):
        self.assertEqual(run_2("0\n3\n0\n1\n-3"), 10)


if __name__ == '__main__':
    unittest.main()
