import json
import random

import boardutils

__author__ = 'Glenn'


class roboplayer:
    def __init__(self):
        self.boardDict = {}

    def loadFromFile(self, filename):
        try:
            with open(filename, 'r') as f:
                self.boardDict = json.load(f)
        except IOError:
            pass

    def saveToFile(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.boardDict, f)

    def _empty(self, boardString):
        boardList = boardutils.blankList(boardString)
        if not boardString in self.boardDict:
            self.boardDict[boardString] = 4 * boardList

    def getMove(self, boardString):
        self._empty(boardString)
        moveList = self.boardDict[boardString]
        assert len(moveList) > 0
        if len(moveList) > 1:
            randomIndex = random.randint(0, len(moveList) - 1)
        else:
            randomIndex = 0
        return moveList[randomIndex]

    def adjust(self, moveList, board, boardDict):
        winner = boardutils.winner(board)
        if winner == 'O':
            for i in range(0, len(moveList), 2):
                movesTuple = moveList[i]
                boardInstance = movesTuple[0]
                movesInstance = movesTuple[1]
                if len(boardDict[boardInstance]) > 1:
                    boardDict[boardInstance].remove(movesInstance)
            for i in range(1, len(moveList), 2):
                movesTuple = moveList[i]
                boardInstance = movesTuple[0]
                movesInstance = movesTuple[1]
                if boardInstance != board:
                    boardDict[boardInstance].append(movesInstance)
                else:
                    boardDict[boardInstance] = [movesInstance]
        elif winner == 'X':
            for i in range(0, len(moveList), 2):
                movesTuple = moveList[i]
                boardInstance = movesTuple[0]
                movesInstance = movesTuple[1]
                if boardInstance != board:
                    boardDict[boardInstance].append(movesInstance)
            for i in range(1, len(moveList), 2):
                movesTuple = moveList[i]
                boardInstance = movesTuple[0]
                movesInstance = movesTuple[1]
                if len(boardDict[boardInstance]) > 1:
                    boardDict[boardInstance].remove(movesInstance)
                else:
                    boardDict[boardInstance] = [movesInstance]
        return boardDict
