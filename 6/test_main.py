#! /usr/bin/env python3

import unittest
from main import run_1, run_2


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(run_1("0\t2\t7\t0"), 5)


if __name__ == '__main__':
    unittest.main()
