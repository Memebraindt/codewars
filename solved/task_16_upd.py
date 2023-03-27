"""
https://www.codewars.com/kata/5296bc77afba8baa690002d7
Sudoku Solver
"""

def valid(puzzle, guess, i, j):
    line_valid = guess not in puzzle[i]
    column_valid = guess not in (puzzle[k][j] for k in range(9))
    subgrid_valid = guess not in (puzzle[i - i % 3 + m][j - j % 3 + n]
                                  for n in range(3)
                                  for m in range(3))
    return line_valid and column_valid and subgrid_valid


def sudoku_solver(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                for guess in range(1, 10):
                    if valid(puzzle, guess, i, j):
                        puzzle[i][j] = guess
                        if sudoku_solver(puzzle):
                             return puzzle
                        puzzle[i][j] = 0
                return False
    return puzzle


puzzle = [[0, 0, 7, 1, 0, 5, 0, 0, 0],
          [5, 0, 0, 2, 0, 0, 1, 3, 0],
          [0, 0, 0, 0, 0, 0, 0, 9, 0],
          # ======================
          [7, 0, 0, 3, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 6],
          [0, 8, 0, 0, 4, 0, 0, 0, 0],
          # =======================
          [0, 0, 0, 6, 0, 0, 0, 0, 7],
          [1, 0, 0, 0, 0, 0, 0, 0, 9],
          [0, 0, 4, 0, 3, 0, 6, 1, 0]]


print(sudoku_solver(puzzle))
