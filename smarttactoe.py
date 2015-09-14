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
        tempBoard = []
        for i in range(len(self.board)):
            if self.board[i] == ' ':
                tempBoard.append(i)
        tempString = ''.join(self.board)
        if not self.board in self.boardDict:
            self.boardDict[tempString] = 4 * tempBoard
        return tempBoard

    # Writes to the file that stores the computer logic
    def saveMatchboxes(self):
        with open(self.FILENAME, 'w') as f:
            json.dump(self.boardDict, f)

    # Determines which player moves next based on the empty spaces in the board
    def toMove(self):
        nextPlayerX = False
        for square in self.board:
            if square == ' ':
                nextPlayerX = not nextPlayerX
        if nextPlayerX:
            return 'X'
        else:
            return 'O'

    # Generates the computer's move by checking blank spaces and selecting one at random
    def generateMove(self):
        boardString = ''.join(self.board)
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

    # Checks if a space is empty, if so checks to see what mark to place.  Returns True if it places a mark at index
    def move(self, nextMove):
        if self.board[nextMove] == ' ':
            boardList = list(self.board)
            boardList[nextMove] = self.toMove()
            self.board = ''.join(boardList)
            return True
        else:
            return False

    # Checks if the game has a winner, or if all spaces are filled w/o a winner then it's a tie
    def winner(self):
        winner = None
        # check horizontal
        if self._checkLine(0, 1, 2):
            winner = self.board[0]
        elif self._checkLine(3, 4, 5):
            winner = self.board[3]
        elif self._checkLine(6, 7, 8):
            winner = self.board[6]
        # check vertical
        elif self._checkLine(0, 3, 6):
            winner = self.board[0]
        elif self._checkLine(1, 4, 7):
            winner = self.board[1]
        elif self._checkLine(2, 5, 8):
            winner = self.board[2]
        # check diagonal
        elif self._checkLine(0, 4, 8):
            winner = self.board[0]
        elif self._checkLine(2, 4, 6):
            winner = self.board[2]
        elif not self._empty():
            winner = 'Cat'
        if winner and winner != 'Cat' and not self.matchBoxesAdjusted:
            logging.debug('Before adjustment')
            self.logMoves()
            self.adjustMatchboxes(winner)
            logging.debug('After adjustment')
            self.logMoves()
            self.matchBoxesAdjusted = True
        if winner:
            self.saveMatchboxes()
        return winner

    # Adjust matchboxes so that move is more likely to happen in the future
    def adjustMatchboxes(self, winner):
        if winner and self.toMove() == 'X':
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
        elif winner and self.toMove() == 'O':
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
        self.board = '         '
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
        while not game.winner() and game.winner() != 'Cat':
            nextMove = game.generateMove()
            logging.debug(nextMove)
            game.move(nextMove)
            print boardutils.readableBoardString(game.board)
        winnerString = game.winner()
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
