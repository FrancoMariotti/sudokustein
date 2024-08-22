import unittest
from sudoku import Sudoku
from sudoku import InvalidMovementError

sudoku_str = """090060500
200000849
007590126
419003000
000908000
003070400
000000250
600020007
002409060"""

almost_finished_sudoku_str = """034678912
672195348
198342567
859761423
426853791
713924856
961537284
287419635
345286179"""

def _load_board(board_str):
    rows = board_str.split('\n')
    return [list(map(int,row)) for row in rows]

class TestSudoku(unittest.TestCase):
    def test_error_should_be_raised_when_trying_to_insert_value_higher_than_nine_into_cell(self):
        with self.assertRaises(ValueError):
            board = _load_board(sudoku_str)
            sudoku = Sudoku(board)
            pos = (1,1)
            value = 10
            sudoku.insert_value_in_pos(value, pos)

    def test_error_should_be_raised_when_trying_to_insert_value_lower_than_1_into_cell(self):
        with self.assertRaises(ValueError):
            board = _load_board(sudoku_str)
            sudoku = Sudoku(board)
            pos = (0,0)
            value = 0
            sudoku.insert_value_in_pos(value, pos)

    def test_is_finished_should_return_false_when_valid_unfinished_sudoku_is_created(self):
        board = _load_board(sudoku_str)
        sudoku = Sudoku(board)
        self.assertFalse(sudoku.finished())
    
    def test_is_finished_should_return_true_when_valid_sodoku_is_finished(self):
        board = _load_board(almost_finished_sudoku_str)
        sudoku = Sudoku(board)
        pos = (0,0)
        value = 5
        sudoku.insert_value_in_pos(value, pos)
        self.assertTrue(sudoku.finished())

    def test_insert_value_in_pos_should_raise_an_error_when_trying_to_insert_value_already_present_in_row(self):
        with self.assertRaises(InvalidMovementError):
            board = _load_board(sudoku_str)
            sudoku = Sudoku(board)
            pos = (0,0)
            value = 5
            sudoku.insert_value_in_pos(value, pos)

    def test_insert_value_in_pos_should_raise_an_error_when_trying_to_insert_value_already_present_in_col(self):
        with self.assertRaises(InvalidMovementError):
            board = _load_board(sudoku_str)
            sudoku = Sudoku(board)
            pos = (0,0)
            value = 2
            sudoku.insert_value_in_pos(value, pos)
    
    def test_insert_value_in_pos_should_raise_an_error_when_trying_to_insert_value_already_present_in_box(self):
        with self.assertRaises(InvalidMovementError):
            board = _load_board(sudoku_str)
            sudoku = Sudoku(board)
            pos = (1,2)
            value = 2
            sudoku.insert_value_in_pos(value, pos)

if __name__ == '__main__':
    unittest.main()
