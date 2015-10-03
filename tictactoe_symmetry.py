import itertools

import boardutils

__author__ = 'Glenn'

IDENTITY_TUPLE = range(9)
ROT90_TUPLE = (6, 3, 0, 7, 4, 1, 8, 5, 2)
ROT180_TUPLE = (8, 7, 6, 5, 4, 3, 2, 1, 0)
ROT270_TUPLE = (2, 5, 8, 1, 4, 7, 0, 3, 6)
VERTICAL_TUPLE = (2, 1, 0, 5, 4, 3, 8, 7, 6)
HORIZONTAL_TUPLE = (6, 7, 8, 3, 4, 5, 0, 1, 2)
LEFT_DIAGONAL_TUPLE = (8, 5, 2, 7, 4, 1, 6, 3, 0)
RIGHT_DIAGONAL_TUPLE = (0, 3, 6, 1, 4, 7, 2, 5, 8)
SYMMETRY_TUPLE = (IDENTITY_TUPLE, ROT90_TUPLE, ROT180_TUPLE, ROT270_TUPLE, VERTICAL_TUPLE, HORIZONTAL_TUPLE,
                  LEFT_DIAGONAL_TUPLE, RIGHT_DIAGONAL_TUPLE)
IDENTITY, ROT90, ROT180, ROT270, VERTICAL, HORIZONTAL, LEFT_DIAGONAL, RIGHT_DIAGONAL = range(8)

# Applies symmetry 0-7 to the board_string supplied
def apply_symmetry(boardString, symmetry):
    return ''.join([boardString[SYMMETRY_TUPLE[symmetry][i]] for i in range(len(boardString))])


def symmetric_boards(boardString):
    return [(apply_symmetry(boardString, i) for i in range(len(SYMMETRY_TUPLE)))]


def canonical_board(boardString):
    symmetric = symmetric_boards(boardString)
    canonical = sorted(symmetric_boards(boardString))
    board_index = symmetric.index(canonical)
    return (canonical, board_index)


def is_canonical(x):
    return x == canonical_board(x)


def is_legal(x):
    return is_canonical(x) and not boardutils.winner(x)


def canon_non_winning(board):
    return len({''.join(b) for b in itertools.ifilter(lambda x: is_legal(''.join(x)),
                                                      itertools.permutations(board))})


if __name__ == '__main__':
    print apply_symmetry('XOXOX    ', ROT90)
    print apply_symmetry(apply_symmetry('XOXOX    ', ROT90), ROT270)
