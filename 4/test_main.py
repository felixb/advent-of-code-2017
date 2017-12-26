#! /usr/bin/env python3

import unittest
from main import run_1, run_2


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(run_1("aa bb cc dd ee\naa bb cc dd aa\naa bb cc dd aaa"), 2)


if __name__ == '__main__':
    unittest.main()
