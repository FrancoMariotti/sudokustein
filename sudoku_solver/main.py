#! /bin/python3
from math import floor

LINE = '-' * 25
COLS = 9
ROWS = 9

COUNTER = 0

maps = [
"""090060500
200000849
007590126
419003000
000908000
003070400
000000250
600020007
002409060"""
]

#board = [
#    ["5","3",".",".","7",".",".",".","."],
#    ["6",".",".","1","9","5",".",".","."],
#    [".","9","8",".",".",".",".","6","."],
#    ["8",".",".",".","6",".",".",".","3"],
#    ["4",".",".","8",".","3",".",".","1"],
#    ["7",".",".",".","2",".",".",".","6"],
#    [".","6",".",".",".",".","2","8","."],
#    [".",".",".","4","1","9",".",".","5"],
#    [".",".",".",".","8",".",".","7","9"]
#]

"""
1   Each of the digits 1-9 must occur exactly once in each row.
2   Each of the digits 1-9 must occur exactly once in each column.
3   Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.  
"""
############### Draw Board #####################

def _append_cell_value(board_str, value):
        return board_str + str(value).ljust(2)

def _append_end_of_row(board_str):
        return board_str + f"| \n"

def _append_line(board_str):
        return board_str + f"{LINE}\n".rjust(len(LINE) + 3)

def print_sudoku(board):
        board_str = "0 1 2   3 4 5   6 7 8 \n".rjust(27)
        for row in range(len(board)):
            if(row % 3 == 0):
                board_str = _append_line(board_str)
            for col in range(len(board[row])):
                if(col % 3 == 0):
                    board_str += f"{row} | " if col == 0 else "| "
                board_str = _append_cell_value(board_str, board[row][col])
            board_str = _append_end_of_row(board_str) 
        print(_append_line(board_str))

############### Solve Board #####################

def round_to_multiple(number, multiple):
    return multiple * floor(number / multiple)

def _is_present_in_box(value,i, j, board):
    initial_row = round_to_multiple(i, 3)
    final_row = initial_row + 3
    initial_col = round_to_multiple(j, 3)
    final_col = initial_col + 3

    for row in range(initial_row, final_row):
        for col in range(initial_col, final_col):
            if value == board[row][col]:
                return True
    return False

def _is_in_row(n, row):
    return n in row

def _is_in_col(n, col, board):
    found = False
    for i in range(len(board)):
        found = found or board[i][col] == n
    return found

def _solve_sudoku(board, value, i=0, j=0):
    if i >= ROWS:
        return True

    next_i = i if j + 1 < COLS else i + 1
    next_j = j + 1 if j + 1 < COLS else 0

    if board[i][j] != 0:
        return _solve_sudoku(board, value, next_i, next_j)

    if _is_in_row(value, board[i]) \
        or _is_in_col(value, j, board) \
        or _is_present_in_box(value, i, j, board):
        return False

    board[i][j] = value

    solved = False
    for digit in range(1, 10): 
        solved = _solve_sudoku(board, digit, next_i, next_j)
        if solved:
            break

    if (not solved):
        board[i][j] = 0

    print_sudoku(board)
    return solved

def solve_sudoku(board):
    for digit in range(1, 10): 
        solved = _solve_sudoku(board, digit)
        if solved:
            break

def main():
    try:
        rows = maps[0].split('\n')
        board = [list(map(int,row)) for row in rows]
        print("sudoku solver")
        print_sudoku(board)
        solve_sudoku(board)
        print("Solution:")
        print_sudoku(board)
    except KeyboardInterrupt:
        print("Simulation Stopped")

main()

