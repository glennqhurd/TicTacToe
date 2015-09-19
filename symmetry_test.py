__author__ = 'Glenn'

import unittest

from tictactoe_symmetry import *


class testRoboplayer(unittest.TestCase):
    def testApplySymmetries(self):
        boardString = ('XO       ')
        identityString = applySymmetries(boardString, 0)
        self.assertEqual(boardString, identityString)
        rot90String = applySymmetries(boardString, 1)
        testString = ('  X  O   ')
        self.assertEqual(testString, rot90String)
        rot180String = applySymmetries(boardString, 2)
        testString = ('       OX')
        self.assertEqual(testString, rot180String)
        rot270String = applySymmetries(boardString, 3)
        testString = ('   O  X  ')
        self.assertEqual(testString, rot270String)
        verticalString = applySymmetries(boardString, 4)
        testString = (' OX      ')
        self.assertEqual(testString, verticalString)
        horizontalString = applySymmetries(boardString, 5)
        testString = ('      XO ')
        self.assertEqual(testString, horizontalString)
        leftDiagonalString = applySymmetries(boardString, 6)
        testString = ('     O  X')
        self.assertEqual(testString, leftDiagonalString)
        rightDiagonalString = applySymmetries(boardString, 7)
        testString = ('X  O     ')
        self.assertEqual(testString, rightDiagonalString)

    def testRotation(self):
        boardString = ('XO       ')
        identityString = identity(boardString)
        self.assertEqual(boardString, identityString)
        Rot90String = Rot90(boardString)
        testString = ('  X  O   ')
        self.assertEqual(testString, Rot90String)
        Rot180String = Rot180(boardString)
        testString = ('       OX')
        self.assertEqual(testString, Rot180String)
        Rot90String = Rot90(Rot90String)
        self.assertEqual(testString, Rot90String)
        Rot270String = Rot270(boardString)
        testString = ('   O  X  ')
        self.assertEqual(testString, Rot270String)
        Rot90String = Rot90(Rot90String)
        self.assertEqual(testString, Rot90String)

    def testVerticalReflection(self):
        boardString = '         '
        newString = flipVertical(boardString)
        self.assertEqual(boardString, newString)
        boardString = 'X O X    '
        newString = flipVertical(boardString)
        testString = 'O X X    '
        self.assertEqual(testString, newString)
        boardString = 'X O O X O'
        newString = flipVertical(boardString)
        testString = 'O X O O X'
        self.assertEqual(testString, newString)

    def testHorizontalReflection(self):
        boardString = '         '
        newString = flipHorizontal(boardString)
        self.assertEqual(boardString, newString)
        boardString = 'X O X    '
        newString = flipHorizontal(boardString)
        testString = '    X X O'
        self.assertEqual(testString, newString)
        boardString = 'X O O O X'
        newString = flipHorizontal(boardString)
        testString = 'O X O X O'
        self.assertEqual(testString, newString)


if __name__ == '__main__':
    unittest.main()
