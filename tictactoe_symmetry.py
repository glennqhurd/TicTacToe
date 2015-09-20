__author__ = 'Glenn'

IDENTITY_TUPLE = (0, 1, 2, 3, 4, 5, 6, 7, 8)
ROT90_TUPLE = (6, 3, 0, 7, 4, 1, 8, 5, 2)
ROT180_TUPLE = (8, 7, 6, 5, 4, 3, 2, 1, 0)
ROT270_TUPLE = (2, 5, 8, 1, 4, 7, 0, 3, 6)
VERTICAL_TUPLE = (2, 1, 0, 5, 4, 3, 8, 7, 6)
HORIZONTAL_TUPLE = (6, 7, 8, 3, 4, 5, 0, 1, 2)
LEFT_DIAGONAL_TUPLE = (8, 5, 2, 7, 4, 1, 6, 3, 0)
RIGHT_DIAGONAL_TUPLE = (0, 3, 6, 1, 4, 7, 2, 5, 8)
SYMMETRY_TUPLE = (IDENTITY_TUPLE, ROT90_TUPLE, ROT180_TUPLE, ROT270_TUPLE, VERTICAL_TUPLE, HORIZONTAL_TUPLE,
                  LEFT_DIAGONAL_TUPLE, RIGHT_DIAGONAL_TUPLE)

# Applies symmetry 0-7 to the boardString supplied
# 0 identity
# 1 Rot90
# 2 Rot180
# 3 Rot270
# 4 flipVertical
# 5 flipHorizontal
# 6 flipDiagonalFromLeft
# 7 flipDiagonalFromRight
def applySymmetry(boardString, symmetry):
    tuple = SYMMETRY_TUPLE[symmetry]
    boardList1 = list(boardString)
    boardList2 = [boardList1[tuple[i]] for i in range(len(boardString))]
    return ''.join(boardList2)


def identity(boardString):
    return boardString


def Rot90(boardString):
    boardList1 = list(boardString)
    boardList2 = []
    for i in range(len(boardString)):
        boardList2.append(boardList1[ROT90_TUPLE[i]])
    return ''.join(boardList2)


def Rot180(boardString):
    boardList1 = list(boardString)
    boardList2 = []
    for i in range(len(boardString)):
        boardList2.append(boardList1[ROT180_TUPLE[i]])
    return ''.join(boardList2)


def Rot270(boardString):
    boardList1 = list(boardString)
    boardList2 = []
    for i in range(len(boardString)):
        boardList2.append(boardList1[ROT270_TUPLE[i]])
    return ''.join(boardList2)


def flipVertical(boardString):
    boardList1 = list(boardString)
    boardList2 = []
    for i in range(len(boardString)):
        boardList2.append(boardList1[VERTICAL_TUPLE[i]])
    return ''.join(boardList2)


def flipHorizontal(boardString):
    boardList1 = list(boardString)
    boardList2 = []
    for i in range(len(boardString)):
        boardList2.append(boardList1[HORIZONTAL_TUPLE[i]])
    return ''.join(boardList2)


def flipDiagonalFromLeft(boardString):
    boardList1 = list(boardString)
    boardList2 = []
    for i in range(len(boardString)):
        boardList2.append(boardList1[LEFT_DIAGONAL_TUPLE[i]])
    return ''.join(boardList2)


def flipDiagonalFromRight(boardString):
    boardList1 = list(boardString)
    boardList2 = []
    for i in range(len(boardString)):
        boardList2.append(boardList1[RIGHT_DIAGONAL_TUPLE[i]])
    return ''.join(boardList2)
