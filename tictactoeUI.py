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
        self.inProgress = False
        self.opponentThread = None
        self.opponentMoveEvent = threading.Event()

    def createWindow(self):
        logging.debug('Entering createWindow')
        board_window = Tk()
        self.radioVariable = IntVar()
        self.radioVariable.set(1)
        Label(board_window, text='Tic-Tac-Toe Matchbox').grid(row=0, column=0, columnspan=2)
        self.boardCanvas = Canvas(board_window, width=300, height=300)
        self.boardCanvas.bind('<Button-1>', self.click)
        self.boardCanvas.grid(row=1, column=0, rowspan=4)
        self.playerLabel = Label(board_window, text='Player 1 turn (X)')
        self.playerLabel.grid(row=5, column=0)
        Button(board_window, text='New Game', command=self.startGame).grid(row=1, column=1)
        self.radioButtonPlayer = Radiobutton(board_window, text="Versus Player", variable=self.radioVariable,
                                             value=PLAYER_MODE, command=self.startGame)
        self.radioButtonPlayer.grid(row=2, column=1, sticky='W')
        self.radioButtonComputer = Radiobutton(board_window, text="Versus Computer", variable=self.radioVariable,
                                               value=COMPUTER_MODE, command=self.startGame)
        self.radioButtonComputer.grid(row=3, column=1)
        self.startGame()
        board_window.mainloop()
        logging.debug('Leaving createWindow')

    def startGame(self):
        logging.debug('Entering startGame')
        self.game.resetBoard()
        self.inProgress = False  # Unfreeze the buttons until click is called.
        self.radioButtonPlayer.config(state='active')
        self.radioButtonComputer.config(state='active')
        self.playerLabel.config(text='Player 1 turn (X)')
        self.boardCanvas.delete("all")
        self.boardCanvas.create_line(0, 100, 300, 100)
        self.boardCanvas.create_line(0, 200, 300, 200)
        self.boardCanvas.create_line(100, 0, 100, 300)
        self.boardCanvas.create_line(200, 0, 200, 300)
        if self.computerOpponent():
            self.opponentThread = threading.Thread(name='opponentThread', target=self.opponentMove)
            self.opponentThread.setDaemon(True)
            self.opponentThread.start()
        logging.debug('Leaving startGame')


    def computerOpponent(self):
        return self.radioVariable.get() == COMPUTER_MODE

    def opponentMove(self):
        logging.debug('Entering opponentMove')
        while self.inProgress and self.computerOpponent():
            self.opponentMoveEvent.wait()
            computerMove = self.robo.getMove(self.game.board)
            self.game.board = boardutils.setMove(self.game.board, computerMove, 'O')
            self.drawO(computerMove)
            self.opponentMoveEvent.clear()
            self.check_for_winner()
        logging.debug('Leaving opponentMove')

    def check_for_winner(self):
        logging.debug('Entering check_for_winner')
        checkWinner = boardutils.winner(self.game.board)
        if boardutils.toMove(self.game.board) == 'X':
            self.playerLabel.config(text='Player 1 turn (X)')
        elif boardutils.toMove(self.game.board) == 'O':
            self.playerLabel.config(text='Player 2 turn (O)')
        if checkWinner == 'X':
            self.playerLabel.config(text='Player 1 wins!')
        elif checkWinner == 'O':
            self.playerLabel.config(text='Player 2 wins!')
        elif checkWinner == 'Cat':
            self.playerLabel.config(text='It\'s a tie!')
        if checkWinner:
            self.inProgress = False
            self.radioButtonPlayer.config(state='active')
            self.radioButtonComputer.config(state='active')
            if self.opponentThread:
                self.endOpponentThread()
        logging.debug('Leaving check_for_winner')

    def endOpponentThread(self):
        self.opponentMoveEvent.set()
        self.opponentThread.join()
        self.opponentThread = None
        self.opponentMoveEvent = None

    def drawX(self, box):
        self.boardCanvas.create_line(((box % 3) * 100 + 20), ((int(box / 3) * 100) + 20), ((box % 3) * 100 + 80),
                                     ((int(box / 3) * 100) + 80))
        self.boardCanvas.create_line(((box % 3) * 100 + 20), ((int(box / 3) * 100) + 80), ((box % 3) * 100 + 80),
                                     ((int(box / 3) * 100) + 20))

    def drawO(self, box):
        self.boardCanvas.create_oval(((box % 3) * 100 + 10), ((int(box / 3) * 100) + 10), ((box % 3) * 100 + 90),
                                     ((int(box / 3) * 100) + 90))

    def click(self, event):
        # Freeze the radio buttons when click occurs.
        if self.computerOpponent() and self.opponentMoveEvent.is_set():
            return
        box = self.boxNumber(event.x, event.y)
        if box == None:
            return
        else:
            self.inProgress = True
            self.radioButtonPlayer.config(state='disabled')
            self.radioButtonComputer.config(state='disabled')
            if boardutils.toMove(self.game.board) == 'X':
                if boardutils.isValidMove(self.game.board, box):
                    self.game.board = boardutils.setMove(self.game.board, box, 'X')
                    self.drawX(box)
                    checkWinner = boardutils.winner(self.game.board)
                    if self.computerOpponent() and checkWinner == None:
                        self.opponentMoveEvent.set()
                else:
                    return
            elif boardutils.toMove(self.game.board) == 'O':
                if boardutils.isValidMove(self.game.board, box):
                    self.game.board = boardutils.setMove(self.game.board, box, 'O')
                    self.drawO(box)
                else:
                    return
            self.check_for_winner()


    def boxNumber(self, x, y):
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
    t.createWindow()
