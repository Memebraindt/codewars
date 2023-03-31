"""
https://www.codewars.com/kata/5588bd9f28dbb06f43000085
Hard Sudoku Solver
"""


def valid(puzzle, guess, i, j):
    line_valid = guess not in puzzle[i]
    column_valid = guess not in (puzzle[k][j] for k in range(9))
    subgrid_valid = guess not in (puzzle[i - i % 3 + m][j - j % 3 + n]
                                  for n in range(3)
                                  for m in range(3))
    return line_valid and column_valid and subgrid_valid


def check_errors(puzzle):
    if len(puzzle) != 9:
        raise RuntimeError("Wrong length of list")
    else:
        for i in puzzle:
            if len(i) != 9:
                raise RuntimeError("Wrong length of list")
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] not in range(0, 10):
                raise RuntimeError("Wrong number")


def sudoku(puzzle):
    check_errors(puzzle)
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                for guess in range(1, 10):
                    if valid(puzzle, guess, i, j):
                        puzzle[i][j] = guess
                        if sudoku(puzzle):
                            return puzzle
                        puzzle[i][j] = 0
                return False
    return puzzle


puzzle2 = [
    [0, 0, 6, 1, 0, 0, 0, 0, 8],
    [0, 8, 0, 0, 9, 0, 0, 3, 0],
    [2, 0, 0, 0, 0, 5, 4, 0, 0],
    [4, 0, 0, 0, 0, 1, 8, 0, 0],
    [0, 3, 0, 0, 7, 0, 0, 4, 0],
    [0, 0, 7, 9, 0, 0, 0, 0, 3],
    [0, 0, 8, 4, 0, 0, 0, 0, 6],
    [0, 2, 0, 0, 5, 0, 0, 8, 0],
    [1, 0, 0, 0, 0, 2, 5, 0, 0]
]

puzzle = [[0, 0, 7, 1, 0, 5, 0, 0, 0],
          [5, 0, 0, 2, 0, 0, 1, 3, 0],
          [0, 0, 0, 0, 0, 0, 0, 9, 0],
          [7, 0, 0, 3, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 6],
          [0, 8, 0, 0, 4, 0, 0, 0, 0],
          [0, 0, 0, 6, 0, 0, 0, 0, 7],
          [1, 0, 0, 0, 0, 0, 0, 0, 9],
          [0, 0, 4, 0, 3, 0, 6, 1, 0]]

print(sudoku(puzzle))
print(sudoku(puzzle2))
