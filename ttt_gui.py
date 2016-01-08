from tkinter import Tk, Button, Label, Frame, StringVar, DISABLED

class Board:
    def __init__(self):
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        self.turn = 'X'
        self.next = 'O'

    def set_cell(self, x, y, var):
        self.board[x][y] = var

    def pop_turn(self):
        tmp = self.turn
        self.turn = self.next
        self.next = tmp
        return tmp

    def win(self):
        if self.win_row():
            return 1
        if self.win_col():
            return 1
        if self.win_dia():
            return 1
        return 0

    def win_row(self):
        for row in self.board:
            if row[0] == row[1] == row[2] == self.next:
                return 1
        return 0

    def win_col(self):
        for a in range(3):
            if self.board[0][a] == self.board[1][a] == self.board[2][a] == self.next:
                return 1
        return 0

    def win_dia(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.next or\
                self.board[2][0] == self.board[1][1] == self.board[0][2] == self.next:
            return 1
        return 0

    def no_empty(self):
        tmp = 0
        for row in self.board:
            for cell in row:
                if cell == '':
                    tmp += 1
        if tmp == 0:
            return 1

class Btn:
    def __init__(self, master, row, col, board, play, fun=0):
        if fun:
            self.button = Button(master, width=1, height=1, command=self.rest, text='rest')
        else:
            self.button = Button(master, width=1, height=1, command=self.clk)
        self.button.grid(row=row, column=col)
        self.row = row
        self.col = col
        self.board = board
        self.play = play
        self.master = master

    def rest(self):
        self.play.restart()

    def clk(self):
        self.button['text'] = self.board.pop_turn()
        self.button['state'] = DISABLED
        self.board.set_cell(self.row, self.col, self.button['text'])
        if self.board.win():
            for btn in self.play.btns:
                btn.button['state'] = DISABLED
            Label(self.master, text='{0} wins!'.format(self.button['text'])).grid(row=4, column=0, columnspan=2)
        elif self.board.no_empty():
            for btn in self.play.btns:
                btn.button['state'] = DISABLED
            Label(self.master, text='Draw!'.format(self.button['text'])).grid(row=4, column=0, columnspan=2)

class Play:
    def __init__(self, master):
        self.master = master
        self.board = Board()
        self.btns = []
        for row in range(3):
            for col in range(3):
                self.btns.append(Btn(master, row, col, self.board, self))
        self.rest = Btn(master, 4, 2, self.board, self, fun=1)

    def restart(self):
        for btn in self.btns:
            btn.button.destroy()
        self.rest.button.destroy()
        self.__init__(self.master)

class Menu:
    def __init__(self, master):
        self.master = master
        master.title("TicTacToe")
        self.label_index = 0
        self.label_text = StringVar()
        self.label_text.set('TicTacToe')
        self.lable = Label(master, textvariable=self.label_text)
        self.lable.pack()
        self.start_button = Button(master, text='Start', command=self.start)
        self.start_button.pack()

    def start(self):
        self.lable.destroy()
        self.start_button.destroy()
        self.play()

    def play(self):
        Play(self.master)

root = Tk()
my_gui = Menu(root)
root.mainloop()
