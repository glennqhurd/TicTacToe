__author__ = 'Glenn'

import unittest

from tictactoe_symmetry import *


class testRoboplayer(unittest.TestCase):
    def testApplySymmetries(self):
        boardString = ('XO       ')
        identityString = applySymmetry(boardString, 0)
        self.assertEqual(boardString, identityString)
        rot90String = applySymmetry(boardString, 1)
        self.assertEqual(('  X  O   '), rot90String)
        rot180String = applySymmetry(boardString, 2)
        self.assertEqual(('       OX'), rot180String)
        rot270String = applySymmetry(boardString, 3)
        self.assertEqual(('   O  X  '), rot270String)
        verticalString = applySymmetry(boardString, 4)
        self.assertEqual((' OX      '), verticalString)
        horizontalString = applySymmetry(boardString, 5)
        self.assertEqual(('      XO '), horizontalString)
        leftDiagonalString = applySymmetry(boardString, 6)
        self.assertEqual(('     O  X'), leftDiagonalString)
        rightDiagonalString = applySymmetry(boardString, 7)
        self.assertEqual(('X  O     '), rightDiagonalString)

    def testRotation(self):
        boardString = ('XO       ')
        identityString = identity(boardString)
        self.assertEqual(boardString, identityString)
        Rot90String = Rot90(boardString)
        self.assertEqual(('  X  O   '), Rot90String)
        Rot180String = Rot180(boardString)
        self.assertEqual(('       OX'), Rot180String)
        Rot90String = Rot90(Rot90String)
        self.assertEqual(('       OX'), Rot90String)
        Rot270String = Rot270(boardString)
        self.assertEqual(('   O  X  '), Rot270String)
        Rot90String = Rot90(Rot90String)
        self.assertEqual(('   O  X  '), Rot90String)

    def testVerticalReflection(self):
        boardString = '         '
        newString = flipVertical(boardString)
        self.assertEqual(boardString, newString)
        boardString = 'X O X    '
        newString = flipVertical(boardString)
        self.assertEqual('O X X    ', newString)
        boardString = 'X O O X O'
        newString = flipVertical(boardString)
        self.assertEqual('O X O O X', newString)

    def testHorizontalReflection(self):
        boardString = '         '
        newString = flipHorizontal(boardString)
        self.assertEqual(boardString, newString)
        boardString = 'X O X    '
        newString = flipHorizontal(boardString)
        self.assertEqual('    X X O', newString)
        boardString = 'X O O O X'
        newString = flipHorizontal(boardString)
        self.assertEqual('O X O X O', newString)


if __name__ == '__main__':
    unittest.main()
