import json
import random

from tictactoe_symmetry import *

__author__ = 'Glenn'

logging.basicConfig(level=logging.INFO)
class roboplayer:
    def __init__(self):
        self.boardDict = {}
        self.load_from_file('move_dict.dat')
        self.move_record = []

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                self.boardDict = json.load(f)
        except IOError:
            pass

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.boardDict, f)

    def _empty(self, board_string):
        canon_board, symmetry = canonical_board(board_string)
        board_list = boardutils.blank_list(canon_board)
        if not canon_board in self.boardDict:
            self.boardDict[canon_board] = 4 * board_list

    def x_move(self, board_string):
        canon_board, symmetry = canonical_board(board_string)
        blanks = boardutils.blank_list(canon_board)
        randomIndex = random.randint(0, len(blanks) - 1)
        symm_move = get_symm_index(blanks[randomIndex], symmetry)
        return symm_move

    def o_move(self, board_string):
        # time.sleep(2)
        self._empty(board_string)
        canon_board, symmetry = canonical_board(board_string)
        moveList = self.boardDict[canon_board]
        assert len(moveList) > 0
        if len(moveList) > 1:
            randomIndex = random.randint(0, len(moveList) - 1)
        else:
            randomIndex = 0
        symm_move = get_symm_index(moveList[randomIndex], symmetry)
        self.move_record.append((canon_board, moveList[randomIndex]))
        return symm_move

    def adjust(self, board):
        winner = boardutils.winner(board)
        move_length = len(self.move_record)
        if winner == 'O':
            for i in range(0, move_length):
                self.record_is_legal()
                board_instance, move = self.move_record[i]
                if board_instance != self.move_record[move_length - 1][0]:
                    self.boardDict[board_instance].extend((move, move, move))
                else:
                    self.boardDict[board_instance] = [move]
        elif winner == 'X':
            for i in range(len(self.move_record)):
                self.record_is_legal()
                board_instance, move = self.move_record[i]
                if len(self.boardDict[board_instance]) > 1:
                    self.boardDict[board_instance].remove(move)
        elif winner == 'Cat':
            for i in range(0, move_length):
                self.record_is_legal()
                board_instance, move = self.move_record[i]
                if board_instance != self.move_record[move_length - 1][0]:
                    self.boardDict[board_instance].append(move)
                else:
                    self.boardDict[board_instance] = [move]
        self.move_record = []
        self.save_to_file('move_dict.dat')

    def record_is_legal(self):
        for i in range(len(self.move_record)):
            board, move = self.move_record[i]
            assert is_canonical(board)
            assert board[move] == ' '

    def reset_record(self):
        self.move_record = []
