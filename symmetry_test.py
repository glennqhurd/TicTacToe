__author__ = 'Glenn'

import unittest

from tictactoe_symmetry import *


class testSymmetry(unittest.TestCase):
    def testApplySymmetries(self):
        boardString = 'XO       '
        self.assertEqual(boardString, applySymmetry(boardString, IDENTITY))
        self.assertEqual('  X  O   ', applySymmetry(boardString, ROT90))
        self.assertEqual('       OX', applySymmetry(boardString, ROT180))
        self.assertEqual('   O  X  ', applySymmetry(boardString, ROT270))
        self.assertEqual(' OX      ', applySymmetry(boardString, VERTICAL))
        self.assertEqual('      XO ', applySymmetry(boardString, HORIZONTAL))
        self.assertEqual('     O  X', applySymmetry(boardString, LEFT_DIAGONAL))
        self.assertEqual('X  O     ', applySymmetry(boardString, RIGHT_DIAGONAL))

    def testSortBoards(self):
        self.assertEqual(['       OX', '      XO ', '     O  X', '   O  X  ', '  X  O   ',
                          ' OX      ', 'X  O     ', 'XO       '], sortBoards('XO       '))

    def testCanonicalBoard(self):
        self.assertEqual('        X', canonicalBoard('X        '))


if __name__ == '__main__':
    unittest.main()
