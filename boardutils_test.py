__author__ = 'Glenn'

import unittest

import boardutils


class TestBoardUtils(unittest.TestCase):
    def testBlankList(self):
        empty_list = boardutils.blank_list('         ')
        self.assertEqual(range(9), empty_list)
        empty_list = boardutils.blank_list('X O X O X')
        self.assertEqual([1, 3, 5, 7], empty_list)

    def testEmptyBoard(self):
        board_string = boardutils.empty_board()
        self.assertEqual(9, len(board_string))
        self.assertEqual(9, board_string.count(' '))

    def testBoardList(self):
        test_list = boardutils.board_list('         ')
        self.assertEqual([' '] * 9, test_list)
        test_list = boardutils.board_list('X O X O X')
        self.assertEqual(['X', ' ', 'O', ' ', 'X', ' ', 'O', ' ', 'X'], test_list)

    def testBoardString(self):
        test_board = boardutils.board_string([' '] * 9)
        self.assertEqual('         ', test_board)
        test_board = boardutils.board_string(['X', ' ', 'O', ' ', 'X', ' ', 'O', ' ', 'X'])
        self.assertEqual('X O X O X', test_board)

    def testWinner(self):
        test_board = boardutils.winner([' '] * 9)
        self.assertEqual(None, test_board)
        test_board = boardutils.winner(['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' '])
        self.assertEqual('X', test_board)
        test_board = boardutils.winner(['O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' '])
        self.assertEqual('O', test_board)
        test_board = boardutils.winner(['X', 'X', 'O', 'O', 'O', 'X', 'X', 'X', 'O'])
        self.assertEqual('Cat', test_board)

    def testToMove(self):
        next_move = boardutils.to_move([' '] * 9)
        self.assertEqual('X', next_move)
        next_move = boardutils.to_move(['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
        self.assertEqual('O', next_move)

    def testSetMove(self):
        modified_board = boardutils.set_move([' '] * 9, 0, 'X')
        expected_board = 'X        '
        self.assertEqual(expected_board, modified_board)
        modified_board = boardutils.set_move(expected_board, 1, 'O')
        expected_board = 'XO       '
        self.assertEqual(expected_board, modified_board)

    def testReadableBoardString(self):
        board_string = 'XO       '
        readable_string = boardutils.readable_board_string(board_string)
        expected_string = (' %s | %s | %s\n'
                          '-----------\n'
                          ' %s | %s | %s\n'
                          '-----------\n'
                           ' %s | %s | %s\n\n' % tuple(board_string))
        self.assertEqual(expected_string, readable_string)
