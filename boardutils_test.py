__author__ = 'Glenn'

import unittest

import boardutils


class TestBoardUtils(unittest.TestCase):
    def testBlankList(self):
        emptyList = boardutils.blank_list('         ')
        self.assertEqual(range(9), emptyList)
        emptyList = boardutils.blank_list('X O X O X')
        self.assertEqual([1, 3, 5, 7], emptyList)

    def testEmptyBoard(self):
        boardString = boardutils.empty_board()
        self.assertEqual(9, len(boardString))
        self.assertEqual(9, boardString.count(' '))

    def testBoardList(self):
        testList = boardutils.board_list('         ')
        self.assertEqual([' '] * 9, testList)
        testList = boardutils.board_list('X O X O X')
        self.assertEqual(['X', ' ', 'O', ' ', 'X', ' ', 'O', ' ', 'X'], testList)

    def testBoardString(self):
        testBoard = boardutils.board_string([' '] * 9)
        self.assertEqual('         ', testBoard)
        testBoard = boardutils.board_string(['X', ' ', 'O', ' ', 'X', ' ', 'O', ' ', 'X'])
        self.assertEqual('X O X O X', testBoard)

    def testWinner(self):
        testBoard = boardutils.winner([' '] * 9)
        self.assertEqual(None, testBoard)
        testBoard = boardutils.winner(['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' '])
        self.assertEqual('X', testBoard)
        testBoard = boardutils.winner(['O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' '])
        self.assertEqual('O', testBoard)
        testBoard = boardutils.winner(['X', 'X', 'O', 'O', 'O', 'X', 'X', 'X', 'O'])
        self.assertEqual('Cat', testBoard)

    def testToMove(self):
        nextMove = boardutils.to_move([' '] * 9)
        self.assertEqual('X', nextMove)
        nextMove = boardutils.to_move(['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
        self.assertEqual('O', nextMove)

    def testSetMove(self):
        modifiedBoard = boardutils.set_move([' '] * 9, 0, 'X')
        expectedBoard = 'X        '
        self.assertEqual(expectedBoard, modifiedBoard)
        modifiedBoard = boardutils.set_move(expectedBoard, 1, 'O')
        expectedBoard = 'XO       '
        self.assertEqual(expectedBoard, modifiedBoard)

    def testReadableBoardString(self):
        boardString = 'XO       '
        readableString = boardutils.readable_board_string(boardString)
        expectedString = (' %s | %s | %s\n'
                          '-----------\n'
                          ' %s | %s | %s\n'
                          '-----------\n'
                          ' %s | %s | %s\n\n' % tuple(boardString))
        self.assertEqual(expectedString, readableString)
