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

# Applies symmetry 0-7 to the boardString supplied
def applySymmetry(boardString, symmetry):
    return ''.join([boardString[SYMMETRY_TUPLE[symmetry][i]] for i in range(len(boardString))])


def sortBoards(boardString):
    return sorted((applySymmetry(boardString, i) for i in range(len(SYMMETRY_TUPLE))))


def canonicalBoard(boardString):
    return sortBoards(boardString)[0]


if __name__ == '__main__':
    print applySymmetry('X        ', RIGHT_DIAGONAL)
