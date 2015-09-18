import json
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
        self.resetBoard()
        self.boardDict = {}
        self.robo.loadFromFile(self.FILENAME)

    # Writes to the file that stores the computer logic
    def saveMatchboxes(self):
        with open(self.FILENAME, 'w') as f:
            json.dump(self.boardDict, f)

    # Returns the board object
    def board(self):
        return self.board

    # Adjust matchboxes so that move is more likely to happen in the future
    def adjustMatchboxes(self, winner):
        if winner and boardutils.toMove(self.board) == 'X':
            for i in range(0, len(self.moves), 2):
                movesTuple = self.moves[i]
                boardInstance = movesTuple[0]
                movesInstance = movesTuple[1]
                if len(self.boardDict[boardInstance]) > 1:
                    self.boardDict[boardInstance].remove(movesInstance)
            for i in range(1, len(self.moves), 2):
                movesTuple = self.moves[i]
                boardInstance = movesTuple[0]
                movesInstance = movesTuple[1]
                if boardInstance != self.board:
                    self.boardDict[boardInstance].append(movesInstance)
                else:
                    self.boardDict[boardInstance] = [movesInstance]
            print 'O wins!'
        elif winner and boardutils.toMove(self.board) == 'O':
            for i in range(0, len(self.moves), 2):
                movesTuple = self.moves[i]
                boardInstance = movesTuple[0]
                movesInstance = movesTuple[1]
                if boardInstance != self.board:
                    self.boardDict[boardInstance].append(movesInstance)
                else:
                    self.boardDict[boardInstance] = [movesInstance]
            for i in range(1, len(self.moves), 2):
                movesTuple = self.moves[i]
                boardInstance = movesTuple[0]
                movesInstance = movesTuple[1]
                if len(self.boardDict[boardInstance]) > 1:
                    self.boardDict[boardInstance].remove(movesInstance)
            print 'X wins!'
        self.robo.saveToFile(self.FILENAME)

    # Resets the board to blank
    def resetBoard(self):
        self.moves = []
        self.board = boardutils.emptyBoard()
        self.matchBoxesAdjusted = False

    # Private methods not expected to be called externally.
    def _checkLine(self, x, y, z):
        return (self.board[x] != ' ' and self.board[x] == self.board[y]
                and self.board[y] == self.board[z])

    def logMoves(self):
        for boardPair in self.moves:
            logging.debug('%s --> %s', boardPair, self.boardDict[boardPair[0]])


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    xTally = 0
    oTally = 0
    catTally = 0
    for i in range(1):
        game = smarttactoe()
        while not boardutils.winner(game.board) and boardutils.winner(game.board) != 'Cat':
            nextMove = game.robo.getMove(game.board)
            logging.debug(nextMove)
            game.board = boardutils.setMove(game.board, nextMove, boardutils.toMove(game.board))
            print boardutils.readableBoardString(game.board)
        winnerString = boardutils.winner(game.board)
        game.adjustMatchboxes(winnerString)
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

            # print 'Winner is %s' % game.winner()
            # print game.boardDict
            # print game.moves
