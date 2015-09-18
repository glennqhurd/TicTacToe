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
        self.inProgress = True
        self.playerMode = True

    def createWindow(self):
        self.BoardWindow = Tk()
        self.radioVariable = IntVar()
        self.radioVariable.set(1)
        Label(self.BoardWindow, text='Tic-Tac-Toe Matchbox').grid(row=0, column=0, columnspan=2)
        self.boardCanvas = Canvas(self.BoardWindow, width=300, height=300)
        self.boardCanvas.bind('<Button-1>', self.click)
        self.boardCanvas.grid(row=1, column=0, rowspan=4)
        self.playerLabel = Label(self.BoardWindow, text='Player 1 turn (X)')
        self.playerLabel.grid(row=5, column=0)
        Button(self.BoardWindow, text='New Game', command=self.drawBoard).grid(row=1, column=1)
        self.radioButtonPlayer = Radiobutton(self.BoardWindow, text="Versus Player", variable=self.radioVariable,
                                             value=PLAYER_MODE, command=lambda: self.setMode(self.radioButtonPlayer))
        self.radioButtonPlayer.grid(row=2, column=1, sticky='W')
        self.radioButtonComputer = Radiobutton(self.BoardWindow, text="Versus Computer", variable=self.radioVariable,
                                               value=COMPUTER_MODE,
                                               command=lambda: self.setMode(self.radioButtonComputer))
        self.radioButtonComputer.grid(row=3, column=1)
        self.drawBoard()
        self.turnCounter = True
        self.BoardWindow.mainloop()

    def drawBoard(self):
        self.game.resetBoard()
        self.inProgress = True
        self.playerLabel.config(text='Player 1 turn (X)')
        self.boardCanvas.delete("all")
        self.boardCanvas.create_line(0, 100, 300, 100)
        self.boardCanvas.create_line(0, 200, 300, 200)
        self.boardCanvas.create_line(100, 0, 100, 300)
        self.boardCanvas.create_line(200, 0, 200, 300)

    def drawX(self, box):
        self.boardCanvas.create_line(((box % 3) * 100 + 20), ((int(box / 3) * 100) + 20), ((box % 3) * 100 + 80),
                                     ((int(box / 3) * 100) + 80))
        self.boardCanvas.create_line(((box % 3) * 100 + 20), ((int(box / 3) * 100) + 80), ((box % 3) * 100 + 80),
                                     ((int(box / 3) * 100) + 20))

    def drawO(self, box):
        self.boardCanvas.create_oval(((box % 3) * 100 + 10), ((int(box / 3) * 100) + 10), ((box % 3) * 100 + 90),
                                     ((int(box / 3) * 100) + 90))

    def click(self, event):
        box = self.boxNumber(event.x, event.y)
        if box == None or self.inProgress != True:
            return
        else:
            if boardutils.toMove(self.game.board) == 'X':
                if boardutils.isValidMove(self.game.board, box):
                    self.game.board = boardutils.setMove(self.game.board, box, 'X')
                    self.drawX(box)
                    if self.radioVariable.get() == PLAYER_MODE:
                        self.playerLabel.config(text='Player 2 turn (O)')
                    elif self.radioVariable.get() == COMPUTER_MODE and \
                                    boardutils.winner(self.game.board) == None:
                        computerMove = self.robo.getMove(self.game.board)
                        self.game.board = boardutils.setMove(self.game.board, computerMove, 'O')
                        self.drawO(computerMove)
                else:
                    return
            elif boardutils.toMove(self.game.board) == 'O':
                if boardutils.isValidMove(self.game.board, box):
                    self.game.board = boardutils.setMove(self.game.board, box, 'O')
                    self.drawO(box)
                    self.playerLabel.config(text='Player 1 turn (X)')
                else:
                    return

            if boardutils.winner(self.game.board) == 'X':
                self.playerLabel.config(text='Player 1 wins!')
                self.inProgress = False
            elif boardutils.winner(self.game.board) == 'O':
                self.playerLabel.config(text='Player 2 wins!')
                self.inProgress = False
            elif boardutils.winner(self.game.board) == 'Cat':
                self.playerLabel.config(text='It\'s a tie!')
                self.inProgress = False

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

    def setMode(self, radio):
        if self.radioVariable.get() == 1:
            self.playerMode = True
        elif self.radioVariable.get() == 2:
            self.playerMode = False
        else:
            print 'error'


if __name__ == '__main__':
    t = tictactoeUI()
    t.createWindow()
