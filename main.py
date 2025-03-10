# main.py

import tkinter as tk
from game2048 import init_board, add_new_number, move_left, move_right, move_up, move_down, is_game_over, has_won, GRID_SIZE

# GitHub: https://github.com/hding2

# interface setup
CELL_SIZE = 100
CELL_PADDING = 10
BACKGROUND_COLOR = "#92877d"
EMPTY_CELL_COLOR = "#9e948a"
CELL_COLORS = {
    0: EMPTY_CELL_COLOR,
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59563",
    32: "#f67c5f",
    64: "#f65e3b",
    128: "#edcf72",
    256: "#edcc61",
    512: "#edc850",
    1024: "#edc53f",
    2048: "#edc22e"
}

TEXT_COLORS = {
    2: "#776e65",
    4: "#776e65",
    8: "#f9f6f2",
    16: "#f9f6f2",
    32: "#f9f6f2",
    64: "#f9f6f2",
    128: "#f9f6f2",
    256: "#f9f6f2",
    512: "#f9f6f2",
    1024: "#f9f6f2",
    2048: "#f9f6f2"
}

FONT = ('Verdana', 24, 'bold')

class Game2048(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title('2048 Game')
        self.grid()
        # mapping keyboard events
        self.master.bind("<Key>", self.key_handler)
        # define mapping of directions and functions
        self.commands = {
            'Up': move_up,
            'Down': move_down,
            'Left': move_left,
            'Right': move_right,
            'w': move_up,
            's': move_down,
            'a': move_left,
            'd': move_right
        }
        self.init_GUI()
        self.board = init_board()
        self.score = 0
        self.update_GUI()

    def init_GUI(self):
        """
        initial game interface, create background and 4*4 grid
        """
        background = tk.Frame(self, bg=BACKGROUND_COLOR, width=CELL_SIZE*GRID_SIZE, height=CELL_SIZE*GRID_SIZE)
        background.grid()
        self.cells = []
        for i in range(GRID_SIZE):
            row = []
            for j in range(GRID_SIZE):
                cell_frame = tk.Frame(background, bg=EMPTY_CELL_COLOR, width=CELL_SIZE, height=CELL_SIZE)
                cell_frame.grid(row=i, column=j, padx=CELL_PADDING, pady=CELL_PADDING)
                cell_number = tk.Label(cell_frame, text='', bg=EMPTY_CELL_COLOR, justify=tk.CENTER,
                                       font=FONT, width=4, height=2)
                cell_number.grid()
                row.append(cell_number)
            self.cells.append(row)

    def update_GUI(self):
        """
        refresh the interface with each cell's number and color
        """
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                value = self.board[i][j]
                if value == 0:
                    self.cells[i][j].configure(text='', bg=CELL_COLORS[0])
                else:
                    self.cells[i][j].configure(text=str(value), bg=CELL_COLORS.get(value, "#ff0000"),
                                               fg=TEXT_COLORS.get(value, "#ffffff"))
        self.update_idletasks()

    def key_handler(self, event):
        """
        handle keyboard event, update grid basing on user's input
        """
        key = event.keysym
        if key in self.commands:
            move_function = self.commands[key]
            new_board, score = move_function(self.board)
            if new_board != self.board:
                self.board = new_board
                self.score += score
                add_new_number(self.board)
                self.update_GUI()
                if has_won(self.board):
                    self.game_over('You win!')
                elif is_game_over(self.board):
                    self.game_over('Game Over!')

    def game_over(self, message):
        """
        give a note when game finished
        """
        game_over_frame = tk.Frame(self, borderwidth=2)
        game_over_frame.place(relx=0.5, rely=0.5, anchor='center')
        tk.Label(game_over_frame, text=message, bg='black', fg='white', font=FONT, padx=10, pady=10).pack()

if __name__ == "__main__":
    Game2048().mainloop()