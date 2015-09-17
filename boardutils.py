__author__ = 'Glenn and Lyman Hurd'
# Note two blank lines before each top-level (i.e., not part of a class) def.

WINNER_TUPLE = ((0, 1, 2), (0, 3, 6), (0, 4, 8), (1, 4, 7),
                (3, 4, 5), (2, 5, 8), (6, 7, 8), (2, 4, 6))


def blankList(boardString):
    """
    Given a board string return a list of the indices that are blank.

    Args:
      boardString: String representing a board position.

    Returns:
      List of indices (ints).
    """
    emptyList = [i for i in range(len(boardString)) if boardString[i] == ' ']
    return emptyList


def winner(boardString):
    """
    Given a board string determine a winner.

    Args:
      boardString: String representing a board position.

    Returns:
      'X', 'O' 'Cat' or None.
    """
    for tuple in WINNER_TUPLE:
        if boardString[tuple[0]] == boardString[tuple[1]] and boardString[tuple[1]] == boardString[tuple[2]]:
            if boardString[tuple[0]] != ' ':
                return boardString[tuple[0]]
    for i in range(len(boardString)):
        if boardString[i] == ' ':
            return None
    return 'Cat'


def setMove(boardString, position, player):
    """
    Return a new board string after making the indicated move.

    Args:
      boardString: String representing a board position.
      position: int between (0-8).
      player: 'X' or 'O'

    Returns:
      New board after move.
    """
    boardList = list(boardString)
    boardList[position] = player
    return ''.join(boardList)


def isValidMove(boardString, position):
    if boardString[position] == ' ':
        return True
    else:
        return False


def readableBoardString(boardString):
    """
    Print a board using ascii characters.
    For testing: Returns a string

    Args:
      boardString: String representing a board position.

    Returns:
      None
    """
    return (' %s | %s | %s\n'
            '-----------\n'
            ' %s | %s | %s\n'
            '-----------\n'
            ' %s | %s | %s\n\n' % tuple(boardString))


def emptyBoard():
    """
    Create a new board string(nine blanks).

    Returns:
      Starting empty board string.
    """
    return '         '


def boardList(boardString):
    """
    Represent a board string as a list.

    Args:
      boardString: Board string.

    Returns:
      List of moves (characters, 'X', "O', ' ').
    """
    return list(boardString)


def boardString(boardList):
    """
    Represent a board list as a string.

    Args:
      boardList: List of moves (characters, 'X', "O', ' ').

    Returns:
      Nine element string.
    """
    return ''.join(boardList)


def toMove(boardString):
    """
    Determine whose move it is from a board string.  The answer will be 'X' if
    there are an off number of blanks and 'O' otherwise.

    Args:
      boardString: Board string.
  ('O', 'X')[boardString.count(' ')%2]
    Returns:
      'X' (odd number of blanks) or 'O' (even number of blanks)
    """
    # HINT: I just found out about a Python function mystring.count(' ') (or
    # any other character).
    return ('O', 'X')[boardString.count(' ') % 2]


if __name__ == '__main__':
    pass
