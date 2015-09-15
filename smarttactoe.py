import json
import logging
import random

import boardutils

__author__ = 'Lyman and Glenn Hurd'

# For reference on MENACE (The matchbox "computer" this is designed after) check out this website:
# http://shorttermmemoryloss.com/menace/

class smarttactoe:
    FILENAME = 'move_dictionary.dat'

    def __init__(self):
        self.resetBoard()
        self.boardDict = {}
        try:
            with open(self.FILENAME, 'r') as f:
                self.boardDict = json.load(f)
        except IOError:
            pass

    # Function to append the indices of the empty spaces on the board into a list, then check to see if the board
    # has been stored already in the boardDict.  If the tempString does not match any boardDict keys, it adds a new key
    # mapped to the empty board spaces list tempBoard.  Then returns tempBoard.
    def _empty(self):
        tempBoard = boardutils.blankList(self.board)
        tempString = boardutils.boardString(self.board)
        if not self.board in self.boardDict:
            self.boardDict[tempString] = 4 * tempBoard

    # Writes to the file that stores the computer logic
    def saveMatchboxes(self):
        with open(self.FILENAME, 'w') as f:
            json.dump(self.boardDict, f)

    # Generates the computer's move by checking blank spaces and selecting one at random
    def generateMove(self):
        boardString = boardutils.boardString(self.board)
        self._empty()
        moveList = self.boardDict[self.board]
        assert len(moveList) > 0
        if len(moveList) > 1:
            randomIndex = random.randint(0, len(moveList) - 1)
        else:
            randomIndex = 0
        self.moves.append((boardString, moveList[randomIndex]))
        return moveList[randomIndex]

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
            nextMove = game.generateMove()
            logging.debug(nextMove)
            game.board = boardutils.setMove(game.board, nextMove, boardutils.toMove(game.board))
            print boardutils.readableBoardString(game.board)
        winnerString = boardutils.winner(game.board)
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
