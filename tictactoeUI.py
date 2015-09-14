from Tkinter import *
from ttk import *

from smarttactoe import *

__author__ = 'Glenn'

PLAYER_MODE = 1
COMPUTER_MODE = 2


class tictactoeUI:
    def __init__(self):
        self.game = smarttactoe()
        self.inProgress = True
        self.playerMode = True

    def createWindow(self):
        self.BoardWindow = Tk()
        self.radioVariable = IntVar()
        self.radioVariable.set(1)
        self.titleLabel = Label(self.BoardWindow, text='Tic-Tac-Toe Matchbox')
        self.titleLabel.grid(row=0, column=0, columnspan=2)
        self.boardCanvas = Canvas(self.BoardWindow, width=300, height=300)
        self.boardCanvas.bind('<Button-1>', self.click)
        self.boardCanvas.grid(row=1, column=0, rowspan=4)
        self.playerLabel = Label(self.BoardWindow, text='Player 1 turn (X)')
        self.playerLabel.grid(row=5, column=0)
        self.newGameButton = Button(self.BoardWindow, text='New Game', command=self.drawBoard)
        self.newGameButton.grid(row=1, column=1)
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
        for i in range(9):
            if box == 0:
                self.boardCanvas.create_line(20, 20, 80, 80)
                self.boardCanvas.create_line(20, 80, 80, 20)
            elif box == 1:
                self.boardCanvas.create_line(120, 20, 180, 80)
                self.boardCanvas.create_line(120, 80, 180, 20)
            elif box == 2:
                self.boardCanvas.create_line(220, 20, 280, 80)
                self.boardCanvas.create_line(220, 80, 280, 20)
            elif box == 3:
                self.boardCanvas.create_line(20, 120, 80, 180)
                self.boardCanvas.create_line(20, 180, 80, 120)
            elif box == 4:
                self.boardCanvas.create_line(120, 120, 180, 180)
                self.boardCanvas.create_line(120, 180, 180, 120)
            elif box == 5:
                self.boardCanvas.create_line(220, 120, 280, 180)
                self.boardCanvas.create_line(220, 180, 280, 120)
            elif box == 6:
                self.boardCanvas.create_line(20, 220, 80, 280)
                self.boardCanvas.create_line(20, 280, 80, 220)
            elif box == 7:
                self.boardCanvas.create_line(120, 220, 180, 280)
                self.boardCanvas.create_line(120, 280, 180, 220)
            elif box == 8:
                self.boardCanvas.create_line(220, 220, 280, 280)
                self.boardCanvas.create_line(220, 280, 280, 220)

    def drawO(self, box):
        for i in range(9):
            if box == 0:
                self.boardCanvas.create_oval(10, 10, 90, 90)
            if box == 1:
                self.boardCanvas.create_oval(110, 10, 190, 90)
            if box == 2:
                self.boardCanvas.create_oval(210, 10, 290, 90)
            if box == 3:
                self.boardCanvas.create_oval(10, 110, 90, 190)
            if box == 4:
                self.boardCanvas.create_oval(110, 110, 190, 190)
            if box == 5:
                self.boardCanvas.create_oval(210, 110, 290, 190)
            if box == 6:
                self.boardCanvas.create_oval(10, 210, 90, 290)
            if box == 7:
                self.boardCanvas.create_oval(110, 210, 190, 290)
            if box == 8:
                self.boardCanvas.create_oval(210, 210, 290, 290)

    def click(self, event):
        box = self.boxNumber(event.x, event.y)
        if box == None or self.inProgress != True:
            return
        else:
            if self.game.toMove() == 'X':
                if self.game.move(box):
                    self.drawX(box)
                    if self.radioVariable.get() == PLAYER_MODE:
                        self.playerLabel.config(text='Player 2 turn (O)')
                    elif self.radioVariable.get() == COMPUTER_MODE and self.game.winner() == None:
                        computerMove = self.game.generateMove()
                        self.game.move(computerMove)
                        self.drawO(computerMove)
            elif self.game.toMove() == 'O':
                if self.game.move(box):
                    self.drawO(box)
                    self.playerLabel.config(text='Player 1 turn (X)')

            if self.game.winner() == 'X':
                self.playerLabel.config(text='Player 1 wins!')
                self.inProgress = False
            elif self.game.winner() == 'O':
                self.playerLabel.config(text='Player 2 wins!')
                self.inProgress = False
            elif self.game.winner() == 'Cat':
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
