__author__ = 'Glenn'

import unittest

import roboplayer
from tictactoe_symmetry import *

logging.basicConfig(level=logging.DEBUG)

class testRoboplayer(unittest.TestCase):
    def test_adjust(self):
        robo = roboplayer.roboplayer()
        # Test if correct when O wins
        board_dict = {canonical_board('         ')[0]: [0, 1], canonical_board('X        ')[0]: [2, 3],
                      canonical_board('X  O     ')[0]: [2, 4], canonical_board('X XO     ')[0]: [4, 5],
                      canonical_board('X XOO    ')[0]: [1, 6], canonical_board('X XOO X  ')[0]: [5, 8]}
        move_list = [(canonical_board('         '), 0), (canonical_board('X        '), 3),
                     (canonical_board('X O      '), 2), (canonical_board('X XO     '), 4),
                     (canonical_board('X XOO    '), 1), (canonical_board('X XOO X  '), 5)]
        new_board_dict = robo.adjust(move_list, 'X XOOOX  ', board_dict)
        test_dict = {canonical_board('         ')[0]: [0, 1], canonical_board('X        ')[0]: [2, 3, 3],
                     canonical_board('X  O     ')[0]: [2, 4], canonical_board('X XO     ')[0]: [4, 5, 4],
                     canonical_board('X XOO    ')[0]: [1, 6], canonical_board('X XOO X  ')[0]: [5, 8, 5]}
        self.assertEqual(test_dict, new_board_dict)
        # Test if correct when X wins
        board_dict = {canonical_board('         ')[0]: [0, 1], canonical_board('X        ')[0]: [2, 3],
                      canonical_board('X  O     ')[0]: [2, 4], canonical_board('X XO     ')[0]: [4, 5],
                      canonical_board('X XOO    ')[0]: [1, 6]}
        move_list = [(canonical_board('         '), 0), (canonical_board('X        '), 3),
                     (canonical_board('X O      '), 2), (canonical_board('X XO     '), 4),
                     (canonical_board('X XOO    '), 1)]
        new_board_dict = robo.adjust(move_list, 'XXXO O   ', board_dict)
        test_dict = {canonical_board('         ')[0]: [0, 1], canonical_board('X        ')[0]: [2],
                     canonical_board('X  O     ')[0]: [2, 4], canonical_board('X XO     ')[0]: [5],
                     canonical_board('X XOO    ')[0]: [1, 6]}
        self.assertEqual(test_dict, new_board_dict)

if __name__ == '__main__':
    unittest.main()
