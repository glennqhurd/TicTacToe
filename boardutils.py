__author__ = 'Glenn and Lyman Hurd'
# Note two blank lines before each top-level (i.e., not part of a class) def.

WINNER_TUPLE = ((0, 1, 2), (0, 3, 6), (0, 4, 8), (1, 4, 7),
                (3, 4, 5), (2, 5, 8), (6, 7, 8), (2, 4, 6))


def blank_list(board_string):
    """
    Given a board string return a list of the indices that are blank.

    Args:
      board_string: String representing a board position.

    Returns:
      List of indices (ints).
    """
    empty_list = [i for i in range(len(board_string)) if board_string[i] == ' ']
    return empty_list


def winner(board_string):
    """
    Given a board string determine a winner.

    Args:
      board_string: String representing a board position.

    Returns:
      'X', 'O' 'Cat' or None.
    """
    assert len(board_string) == 9
    for tuple in WINNER_TUPLE:
        if board_string[tuple[0]] == board_string[tuple[1]] and board_string[tuple[1]] == board_string[tuple[2]]:
            if board_string[tuple[0]] != ' ':
                return board_string[tuple[0]]
    for i in range(len(board_string)):
        if board_string[i] == ' ':
            return None
    return 'Cat\'s Game'


def set_move(board_string, position, player):
    """
    Return a new board string after making the indicated move.

    Args:
      board_string: String representing a board position.
      position: int between (0-8).
      player: 'X' or 'O'

    Returns:
      New board after move.
    """
    board_list = list(board_string)
    board_list[position] = player
    return ''.join(board_list)


def is_valid_move(board_string, position):
    if board_string[position] == ' ':
        return True
    else:
        return False


def readable_board_string(board_string):
    """
    Print a board using ascii characters.
    For testing: Returns a string

    Args:
      board_string: String representing a board position.

    Returns:
      None
    """
    return (' %s | %s | %s\n'
            '-----------\n'
            ' %s | %s | %s\n'
            '-----------\n'
            ' %s | %s | %s\n\n' % tuple(board_string))


def empty_board():
    """
    Create a new board string(nine blanks).

    Returns:
      Starting empty board string.
    """
    return '         '


def board_list(board_string):
    """
    Represent a board string as a list.

    Args:
      board_string: Board string.

    Returns:
      List of moves (characters, 'X', "O', ' ').
    """
    return list(board_string)


def board_string(board_list):
    """
    Represent a board list as a string.

    Args:
      board_list: List of moves (characters, 'X', "O', ' ').

    Returns:
      Nine element string.
    """
    return ''.join(board_list)


def to_move(board_string):
    """
    Determine whose move it is from a board string.  The answer will be 'X' if
    there are an off number of blanks and 'O' otherwise.

    Args:
      board_string: Board string.
  ('O', 'X')[board_string.count(' ')%2]
    Returns:
      'X' (odd number of blanks) or 'O' (even number of blanks)
    """
    # HINT: I just found out about a Python function mystring.count(' ') (or
    # any other character).
    return ('O', 'X')[board_string.count(' ') % 2]


if __name__ == '__main__':
    pass
