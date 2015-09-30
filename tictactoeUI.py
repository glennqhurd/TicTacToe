import threading
from Tkinter import *
from ttk import *

from smarttactoe import *

__author__ = 'Glenn'

PLAYER_MODE = 1
COMPUTER_MODE = 2


class tictactoeUI:
    def __init__(self):
        self.game = smarttactoe()
        self.robo = roboplayer.roboplayer()
        self.in_progress = False
        self.opponent_thread = threading.Thread(name='opponent_thread', target=self.opponent_move)
        self.opponent_thread.setDaemon(True)
        self.opponent_move_event = threading.Event()
        self.opponent_thread.start()

    def create_window(self):
        logging.debug('Entering create_window')
        board_window = Tk()
        self.radio_variable = IntVar()
        self.radio_variable.set(1)
        Label(board_window, text='Tic-Tac-Toe Matchbox').grid(row=0, column=0, columnspan=2)
        self.board_canvas = Canvas(board_window, width=300, height=300)
        self.board_canvas.bind('<Button-1>', self.click)
        self.board_canvas.grid(row=1, column=0, rowspan=4)
        self.player_label = Label(board_window, text='Player 1 turn (X)')
        self.player_label.grid(row=5, column=0)
        Button(board_window, text='New Game', command=self.start_game).grid(row=1, column=1)
        self.radiobutton_player = Radiobutton(board_window, text="Versus Player", variable=self.radio_variable,
                                              value=PLAYER_MODE, command=self.start_game)
        self.radiobutton_player.grid(row=2, column=1, sticky='W')
        self.radiobutton_computer = Radiobutton(board_window, text="Versus Computer", variable=self.radio_variable,
                                                value=COMPUTER_MODE, command=self.start_game)
        self.radiobutton_computer.grid(row=3, column=1)
        self.start_game()
        board_window.mainloop()
        logging.debug('Leaving create_window')

    def start_game(self):
        logging.debug('Entering start_game')
        self.game.reset_board()
        self.in_progress = False  # Unfreeze the buttons until click is called.
        self.radiobutton_player.config(state='active')
        self.radiobutton_computer.config(state='active')
        self.player_label.config(text='Player 1 turn (X)')
        self.board_canvas.delete("all")
        self.board_canvas.create_line(0, 100, 300, 100)
        self.board_canvas.create_line(0, 200, 300, 200)
        self.board_canvas.create_line(100, 0, 100, 300)
        self.board_canvas.create_line(200, 0, 200, 300)
        logging.debug('Leaving start_game')

    def computer_opponent(self):
        return self.radio_variable.get() == COMPUTER_MODE

    def opponent_move(self):
        logging.debug('Entering opponent_move')
        while True:
            if boardutils.to_move(self.game.board) == 'O':
                self.opponent_move_event.wait()
                computer_move = self.robo.getMove(self.game.board)
                self.game.board = boardutils.set_move(self.game.board, computer_move, 'O')
                self.drawO(computer_move)
                self.opponent_move_event.clear()
                self.check_for_winner()
        logging.debug('Leaving opponent_move')

    def check_for_winner(self):
        logging.debug('Entering check_for_winner')
        check_winner = boardutils.winner(self.game.board)
        if boardutils.to_move(self.game.board) == 'X':
            self.player_label.config(text='Player 1 turn (X)')
        elif boardutils.to_move(self.game.board) == 'O':
            self.player_label.config(text='Player 2 turn (O)')
        if check_winner == 'X':
            self.player_label.config(text='Player 1 wins!')
        elif check_winner == 'O':
            self.player_label.config(text='Player 2 wins!')
        elif check_winner == 'Cat':
            self.player_label.config(text='It\'s a tie!')
        if check_winner:
            self.in_progress = False
            self.radiobutton_player.config(state='active')
            self.radiobutton_computer.config(state='active')
        logging.debug('Leaving check_for_winner')

    def drawX(self, box):
        self.board_canvas.create_line(((box % 3) * 100 + 20), ((int(box / 3) * 100) + 20), ((box % 3) * 100 + 80),
                                     ((int(box / 3) * 100) + 80))
        self.board_canvas.create_line(((box % 3) * 100 + 20), ((int(box / 3) * 100) + 80), ((box % 3) * 100 + 80),
                                     ((int(box / 3) * 100) + 20))

    def drawO(self, box):
        self.board_canvas.create_oval(((box % 3) * 100 + 10), ((int(box / 3) * 100) + 10), ((box % 3) * 100 + 90),
                                     ((int(box / 3) * 100) + 90))

    def click(self, event):
        logging.debug('Entering click')
        # Freeze the radio buttons when click occurs.
        if self.computer_opponent() and self.opponent_move_event.is_set():
            return
        box = self.box_number(event.x, event.y)
        if box == None:
            return
        else:
            if self.in_progress == False:
                self.in_progress = True
                self.radiobutton_player.config(state='disabled')
                self.radiobutton_computer.config(state='disabled')
            if boardutils.to_move(self.game.board) == 'X':
                if boardutils.is_valid_move(self.game.board, box):
                    self.game.board = boardutils.set_move(self.game.board, box, 'X')
                    self.drawX(box)
                    check_winner = boardutils.winner(self.game.board)
                    if self.computer_opponent() and check_winner == None:
                        self.opponent_move_event.set()
                else:
                    return
            elif boardutils.to_move(self.game.board) == 'O':
                if boardutils.is_valid_move(self.game.board, box):
                    self.game.board = boardutils.set_move(self.game.board, box, 'O')
                    self.drawO(box)
                else:
                    return
            self.check_for_winner()
        logging.debug('Leaving click')

    def box_number(self, x, y):
        # If clicked on a line returns None
        if x > 5 and x < 95:
            if y > 5 and y < 95:
                return 0
            elif y > 105 and y < 195:
                return 3
            elif y > 205 and y < 295:
                return 6
        elif x > 105 and x < 195:
            if y > 5 and y < 95:
                return 1
            elif y > 105 and y < 195:
                return 4
            elif y > 205 and y < 295:
                return 7
        elif x > 205 and x < 295:
            if y > 5 and y < 95:
                return 2
            elif y > 105 and y < 195:
                return 5
            elif y > 205 and y < 295:
                return 8


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    t = tictactoeUI()
    t.create_window()
