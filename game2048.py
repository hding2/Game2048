# game2048.py

import random
# GitHub: https://github.com/hding2

GRID_SIZE = 4

def init_board():
    # create a 4*4 matrix, 0 represents empty
    board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    # randomly generate two initial number 2
    add_new_number(board)
    add_new_number(board)
    return board

def add_new_number(board):
    empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if board[i][j] == 0]
    if not empty_cells:
        return
    i, j = random.choice(empty_cells)
    board[i][j] = 2

def move_left(board):
    new_board = []
    score = 0  # stat the merging score
    for row in board:
        # find the non-zero numbers
        filtered = [num for num in row if num != 0]
        # merge the same and adjacent numbers
        merged = []
        skip = False
        for i in range(len(filtered)):
            if skip:
                skip = False
                continue
            if i + 1 < len(filtered) and filtered[i] == filtered[i+1]:
                merged.append(filtered[i]*2)
                score += filtered[i]*2
                skip = True
            else:
                merged.append(filtered[i])
        # make up the empty cells
        merged += [0]*(GRID_SIZE - len(merged))
        new_board.append(merged)
    return new_board, score

def reverse_board(board):
    # reverse all rows # move_right = reverse + move_left + reverse
    return [row[::-1] for row in board]

def transpose_board(board):
    # move up = transpose + move_left + transpose; # move down = transpose + reverse+ move_left
    return [list(row) for row in zip(*board)]

def move_right(board):
    # move_right = reverse + move_left + reverse
    reversed_board = reverse_board(board)
    moved_board, score = move_left(reversed_board)
    final_board = reverse_board(moved_board)
    return final_board, score

def move_up(board):
    # move up = transpose + move_left + transpose;
    transposed_board = transpose_board(board)
    moved_board, score = move_left(transposed_board)
    final_board = transpose_board(moved_board)
    return final_board, score

def move_down(board):
    # move down = transpose + move_right + transpose
    transposed_board = transpose_board(board)
    moved_board, score = move_right(transposed_board)
    final_board = transpose_board(moved_board)
    return final_board, score

def is_game_over(board):
    # check if still empty existing
    if any(0 in row for row in board):
        return False
    # check if same adjacent numbers can be merged
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE-1):
            if board[i][j] == board[i][j+1]:
                return False
    for j in range(GRID_SIZE):
        for i in range(GRID_SIZE-1):
            if board[i][j] == board[i+1][j]:
                return False
    return True

def has_won(board):
    return any(2048 in row for row in board)
