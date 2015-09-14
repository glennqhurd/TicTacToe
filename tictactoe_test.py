__author__ = 'Glenn'

import unittest

from smarttactoe import *


class TestTicTacToeMethods(unittest.TestCase):
    def test_empty(self):
        pass
        # self.smart = smarttactoe()
        # self.assertEqual(self.smart._empty(), '0 1 2 3 4 5 6 7 8')

    def testGenerateMove(self):
        self.smart = smarttactoe()


if __name__ == '__main__':
    unittest.main()
