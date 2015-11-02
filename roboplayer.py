import json

from tictactoe_symmetry import *

__author__ = 'Glenn'

logging.basicConfig(level=logging.INFO)
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
        logging.info(winner)
        if winner == 'O':
            for i in range(1, len(moveList), 2):
                movesTuple = moveList[i]
                logging.debug(movesTuple)
                boardInstance = canonical_board(movesTuple[0][0])
                canonBoard = canonical_board(board)
                if boardInstance[0] != canonBoard[0]:
                    logging.debug(boardInstance)
                    logging.debug(movesTuple[1])
                    boardDict[boardInstance[0]].append(movesTuple[1])
                else:
                    boardDict[boardInstance[0]] = [movesTuple[1]]
        elif winner == 'X':
            for i in range(1, len(moveList), 2):
                movesTuple = moveList[i]
                logging.debug(movesTuple)
                boardInstance = canonical_board(movesTuple[0][0])
                canonBoard = canonical_board(board)
                if boardInstance[0] != canonBoard[0]:
                    logging.debug(boardInstance)
                    logging.debug(movesTuple[1])
                    boardDict[boardInstance[0]].remove(movesTuple[1])
                else:
                    boardDict[boardInstance[0]] = [movesTuple[1]]
        return boardDict