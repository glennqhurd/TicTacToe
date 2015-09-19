__author__ = 'Glenn'

ROT90_TUPLE = (6, 3, 0, 7, 4, 1, 8, 5, 2)
ROT180_TUPLE = (8, 7, 6, 5, 4, 3, 2, 1, 0)
ROT270_TUPLE = (2, 5, 8, 1, 4, 7, 0, 3, 6)
VERTICAL_TUPLE = (2, 1, 0, 5, 4, 3, 8, 7, 6)
HORIZONTAL_TUPLE = (6, 7, 8, 3, 4, 5, 0, 1, 2)
LEFT_DIAGONAL_TUPLE = (8, 5, 2, 7, 4, 1, 6, 3, 0)
RIGHT_DIAGONAL_TUPLE = (0, 3, 6, 1, 4, 7, 2, 5, 8)

# Applies symmetry 0-7 to the boardString supplied
# 0 identity
# 1 Rot90
# 2 Rot180
# 3 Rot270
# 4 flipVertical
# 5 flipHorizontal
# 6 flipDiagonalFromLeft
# 7 flipDiagonalFromRight
def applySymmetries(boardString, symmetry):
    if symmetry == 0:
        return identity(boardString)
    elif symmetry == 1:
        return Rot90(boardString)
    elif symmetry == 2:
        return Rot180(boardString)
    elif symmetry == 3:
        return Rot270(boardString)
    elif symmetry == 4:
        return flipVertical(boardString)
    elif symmetry == 5:
        return flipHorizontal(boardString)
    elif symmetry == 6:
        return flipDiagonalFromLeft(boardString)
    elif symmetry == 7:
        return flipDiagonalFromRight(boardString)


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
