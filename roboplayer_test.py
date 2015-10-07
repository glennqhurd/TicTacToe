__author__ = 'Glenn'

import unittest

import roboplayer
from tictactoe_symmetry import *


class testRoboplayer(unittest.TestCase):
    def test_adjust(self):
        robo = roboplayer.roboplayer()
        board_dict = {'         ': [0, 1], 'X        ': [2, 3], 'X  O     ': [2, 4], 'X XO     ': [4, 5],
                      'X XOO     ': [1, 6]}
        move_list = [('         ', 0), ('X        ', 3), ('X O      ', 2), ('X XO     ', 4), ('X XOO    ', 1)]
        board = 'XXXOO    '
        new_board_dict = robo.adjust(move_list, board, board_dict)
        test_dict = {'         ': [0, 1], 'X        ': [2], 'X  O     ': [2, 4], 'X XO     ': [5], 'X XOO     ': [1, 6]}
        self.assertEqual(test_dict['X        '], new_board_dict['X        '])
        board_dict = {canonical_board('         '): [0, 1], canonical_board('X        '): [2, 3],
                      canonical_board('X  O     '): [2, 4], canonical_board('X XO     '): [4, 5],
                      canonical_board('X XOO    '): [1, 6], canonical_board('X XOO X  '): [5, 7]}
        move_list = [(canonical_board('         '), 0), (canonical_board('X        '), 3),
                     (canonical_board('X O      '), 2), (canonical_board('X XO     '), 4),
                     (canonical_board('X XOO    '), 6), (canonical_board('X XOO X  '), 5)]
        board, symmetry = canonical_board('X XOOOX  ')
        new_board_dict = robo.adjust(move_list, board, board_dict)
        test_dict = {canonical_board('         ')[0]: [1], canonical_board('X        ')[0]: [2, 3],
                     canonical_board('X  O     ')[0]: [4], canonical_board('X XO     ')[0]: [4, 5],
                     canonical_board('X XOO    ')[0]: [1], canonical_board('X XOO X  ')[0]: [5, 7]}
        self.assertEqual(test_dict['         '], new_board_dict['         '])


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
