__author__ = 'Glenn'

import unittest

from tictactoe_symmetry import *


class testSymmetry(unittest.TestCase):
    def testApplySymmetries(self):
        boardString = 'XO       '
        canon_string = canonical_board(boardString)
        self.assertEqual('XO       ', apply_symmetry(boardString, IDENTITY))
        self.assertEqual('  X  O   ', apply_symmetry(boardString, ROT90))
        self.assertEqual('       OX', apply_symmetry(boardString, ROT180))
        self.assertEqual('   O  X  ', apply_symmetry(boardString, ROT270))
        self.assertEqual(' OX      ', apply_symmetry(boardString, VERTICAL))
        self.assertEqual('      XO ', apply_symmetry(boardString, HORIZONTAL))
        self.assertEqual('     O  X', apply_symmetry(boardString, LEFT_DIAGONAL))
        self.assertEqual('X  O     ', apply_symmetry(boardString, RIGHT_DIAGONAL))

    def testSymmetricBoards(self):
        self.assertEqual([apply_symmetry('XO       ', i) for i in range(8)], symmetric_boards('XO       '))

    def testCanonicalBoard(self):
        self.assertEqual(('        X', 2), canonical_board('X        '))
        self.assertEqual(('       OX', 2), canonical_board('XO       '))

    def test_get_symm_index(self):
        self.assertEqual(0, get_symm_index(0, 0))
        self.assertEqual(6, get_symm_index(0, 1))
        self.assertEqual(7, get_symm_index(1, 2))

if __name__ == '__main__':
    unittest.main()
