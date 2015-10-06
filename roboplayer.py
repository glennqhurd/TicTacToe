import json

from tictactoe_symmetry import *

__author__ = 'Glenn'

class roboplayer:
    def __init__(self):
        self.boardDict = {}

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                self.boardDict = json.load(f)
        except IOError:
            pass

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.boardDict, f)

    def _empty(self, boardString):
        boardList = boardutils.blank_list(boardString)
        if not boardString in self.boardDict:
            self.boardDict[boardString] = 4 * boardList

    def get_move(self, boardString):
        # time.sleep(2)
        self._empty(boardString)
        moveList = self.boardDict[boardString]
        assert len(moveList) > 0
        # if len(moveList) > 1:
        #     randomIndex = random.randint(0, len(moveList) - 1)
        # else:
        randomIndex = 0
        return moveList[randomIndex]

    def adjust(self, moveList, board, boardDict):
        winner = boardutils.winner(board)
        if winner == 'O':
            for i in range(1, len(moveList), 2):
                movesTuple = moveList[i]
                boardInstance = canonical_board(movesTuple[0])
                if boardInstance[0] != board:
                    boardDict[boardInstance[0]].append(movesTuple[1])
                else:
                    boardDict[boardInstance[0]] = [movesTuple[1]]
        elif winner == 'X':
            for i in range(1, len(moveList), 2):
                movesTuple = moveList[i]
                boardInstance = movesTuple[0]
                if len(boardDict[boardInstance]) > 1:
                    boardDict[boardInstance].remove(movesTuple[1])
                else:
                    boardDict[boardInstance] = [movesTuple[1]]
        return boardDict