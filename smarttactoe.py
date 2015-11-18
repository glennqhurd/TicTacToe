import logging

import roboplayer
import boardutils

__author__ = 'Lyman and Glenn Hurd'

# For reference on MENACE (The matchbox "computer" this is designed after) check out this website:
# http://shorttermmemoryloss.com/menace/

class smarttactoe:
    FILENAME = 'move_dictionary.dat'

    def __init__(self):
        self.robo = roboplayer.roboplayer()
        self.reset_board()
        self.boardDict = {}

    # Returns the board object
    def board(self):
        return self.board

    def add_move(self, board, input_move):
        self.moves[board] = input_move

    # Resets the board to blank
    def reset_board(self):
        self.moves = {}
        self.board = boardutils.empty_board()
        self.matchBoxesAdjusted = False

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    xTally = 0
    oTally = 0
    catTally = 0
    robo = roboplayer.roboplayer()
    for i in range(20):
        game = smarttactoe()
        while not boardutils.winner(game.board) and boardutils.winner(game.board) != 'Cat':
            if boardutils.to_move(game.board) == 'X':
                nextMove = robo.x_move(game.board)
                game.board = boardutils.set_move(game.board, nextMove, boardutils.to_move(game.board))
            else:
                nextMove = robo.o_move(game.board)
                game.board = boardutils.set_move(game.board, nextMove, boardutils.to_move(game.board))
            print boardutils.readable_board_string(game.board)
        winnerString = boardutils.winner(game.board)
        robo.adjust(game.board)
        if winnerString == 'X':
            xTally += 1
        elif winnerString == 'O':
            oTally += 1
        else:
            catTally += 1
        if i % 50 == 0:
            logging.info('X: %d, O: %d, Cat: %d', xTally, oTally, catTally)
            xTally = 0
            oTally = 0
            catTally = 0