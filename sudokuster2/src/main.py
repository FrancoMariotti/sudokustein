from maps import maps
from sudoku import Sudoku
from sudoku import InvalidMovementError

def load_sudoku():
    with open("sudokus.txt", "r") as f:
        sudoku = [f.readline() for _ in range(9)]
        return "".join(sudoku)

def exit(command):
    return command.lower() == "salir"

def main():
    #sudoku_string = load_sudoku()
    sudoku_string = maps[0]
    rows = sudoku_string.split('\n')
    board = [list(map(int,row)) for row in rows]
    sudoku = Sudoku(board)

    while (not sudoku.finished()):
        print(sudoku)
        command = input("Insert command:")
        if(exit(command)):
            break
        row, col, value = map(int, command.split())
        pos = (col, row)
        try:
            sudoku.insert_value_in_pos(value, pos)
        except InvalidMovementError:
            print("Oops! Movimiento invalido!")
        except ValueError:
            print("Oops! Valor ingresado invalido!")
        except IndexError:
            print("Oops! Posicion ingresada invalida!")
main()
