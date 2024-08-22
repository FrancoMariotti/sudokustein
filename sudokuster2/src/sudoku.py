from utils import round_to_multiple

SEPARATOR = '\n'
LINE = '-' * 25
COL = 0
ROW = 1

class InvalidMovementError(Exception):
    pass

class Sudoku:
    def __init__(self, board):
        self.board = board

    def _is_present_in_row(self, value, row):
        return (value in self.board[row])
        
    def _is_present_in_col(self, value, col):
        return True if value == (row[col] for row in self.board) else False
    
    def _is_present_in_box(self, value, pos):
        initial_row = round_to_multiple(pos[ROW], 3)
        final_row = initial_row + 3
        initial_col = round_to_multiple(pos[COL], 3)
        final_col = initial_col + 3
        
        for row in range(initial_row, final_row):
            for col in range(initial_col, final_col):
                if value == self.board[row][col]:
                    return True
        return False

    def _can_insert_value_in_pos(self, value, pos):
        return (not self._is_present_in_row(value, pos[ROW]) 
            and not self._is_present_in_col(value, pos[COL])
            and not self._is_present_in_box(value, pos))

    def insert_value_in_pos(self, value, pos):
        if (pos[ROW] < 0 or pos[ROW] > 8):
            raise IndexError("Row value out of range")

        if (pos[COL] < 0 or pos[COL] > 8):
            raise IndexError("Col value out of range")

        if (value < 1 or value > 9):
            raise ValueError("Value must be in the range of 1 to 9")
            
        if (not self._can_insert_value_in_pos(value, pos)):
            raise InvalidMovementError()

        self.board[pos[ROW]][pos[COL]] = value

    def _board_has_empty_cells(self):
        for row in self.board:
            if (0 in row):
                return True
        return False

    def finished(self):
        return not self._board_has_empty_cells()

    def __append_line(self, board_str):
        return board_str + f"{LINE}\n".rjust(len(LINE) + 3)
    
    def __append_cell_value(self, board_str, value):
        return board_str + str(value).ljust(2)
    
    def __append_end_of_row(self, board_str):
        return board_str + f"| \n"
    
    def __str__(self):
        board_str = "0 1 2   3 4 5   6 7 8 \n".rjust(27)
        for row_index in range(len(self.board)):
            if(row_index % 3 == 0):
                board_str = self.__append_line(board_str)
            for col_index in range(len(self.board[row_index])):
                if(col_index % 3 == 0):
                    board_str += f"{row_index} | " if col_index == 0 else "| "
                board_str = self.__append_cell_value(board_str, self.board[row_index][col_index])
            board_str = self.__append_end_of_row(board_str) 
        return self.__append_line(board_str)

