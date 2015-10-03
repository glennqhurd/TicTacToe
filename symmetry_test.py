__author__ = 'Glenn'

import unittest

from tictactoe_symmetry import *


class testSymmetry(unittest.TestCase):
    def testApplySymmetries(self):
        boardString = 'XO       '
        canon_string = canonical_board(boardString)
        self.assertEqual((canon_string, IDENTITY), apply_symmetry(boardString, IDENTITY))
        self.assertEqual('  X  O   ', apply_symmetry(boardString, ROT90))
        self.assertEqual('       OX', apply_symmetry(boardString, ROT180))
        self.assertEqual('   O  X  ', apply_symmetry(boardString, ROT270))
        self.assertEqual(' OX      ', apply_symmetry(boardString, VERTICAL))
        self.assertEqual('      XO ', apply_symmetry(boardString, HORIZONTAL))
        self.assertEqual('     O  X', apply_symmetry(boardString, LEFT_DIAGONAL))
        self.assertEqual('X  O     ', apply_symmetry(boardString, RIGHT_DIAGONAL))

    def testSymmetricBoards(self):
        self.assertEqual(['       OX', '      XO ', '     O  X', '   O  X  ', '  X  O   ',
                          ' OX      ', 'X  O     ', 'XO       '], symmetric_boards('XO       '))

    def testCanonicalBoard(self):
        self.assertEqual('        X', canonical_board('X        '))


if __name__ == '__main__':
    unittest.main()
