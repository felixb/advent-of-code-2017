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

    def test_2_1(self):
        self.assertEqual(run_2("1"), 2)

    def test_2_2(self):
        self.assertEqual(run_2("2"), 4)

    def test_2_3(self):
        self.assertEqual(run_2("3"), 4)

    def test_2_5(self):
        self.assertEqual(run_2("5"), 10)


if __name__ == '__main__':
    unittest.main()
