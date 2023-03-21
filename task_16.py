"""
https://www.codewars.com/kata/5296bc77afba8baa690002d7
Sudoku Solver
"""


def check_matrix(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 0:
                return False
    return True


def check_row(a, row):
    res = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if a[row][i] != 0:
            res.remove(a[row][i])
    return res


def check_column(a, col):
    res = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for j in range(9):
        if a[j][col] != 0:
            res.remove(a[j][col])
    return res


def check_square(a, x, y):
    res = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x, y = x//3, y//3
    x *= 3
    y *= 3
    for i in range(3):
        for j in range(3):
            if a[x+i][y+j] != 0:
                res.remove(a[x+i][y+j])
    return res


def check_all(a, x, y):
    l1 = check_row(a, x)
    l2 = check_column(a, y)
    l3 = check_square(a, x, y)
    l0 = list(set(list(set(l1).intersection(l2))).intersection(l3))
    return l0


def sudoku(puzzle):
    while not check_matrix(puzzle):
        res = []
        upd = puzzle
        for i in range(9):
            res.append([])
            for j in range(9):
                if puzzle[i][j] != 0:
                    res[i].append(puzzle[i][j])
                else:
                    qq = check_all(puzzle, i, j)
                    if len(qq) != 1:
                        res[i].append(qq)
                    else:
                        puzzle[i][j] = qq[0]
        unique = [[0]*9]*2
        uni_sqr =[[[0]*3]*3]
        for i in range(9):
            for j in range(9):

                for x in range(len(res[i][j])):
                    unique[res[i][j][x]][0] += 1
                    unique[res[i][j][x]][1] += 1
                    uni_sqr[i//3][j//3].append(res[i][j][x])



        if upd == puzzle:
            print("Не нашёл решение :(")
            for i in range(len(res)):
                print()
                for j in range(len(res[i])):
                    print("{:18}".format(str(res[i][j])), end=", ")
            # print(puzzle)
            return 0
    return puzzle


puzzle = [[0,0,7,1,0,5,0,0,0],
           [5,0,0,2,0,0,1,3,0],
           [0,0,0,0,0,0,0,9,0],
           [7,0,0,3,0,0,2,5,0],
           [0,0,0,0,0,0,0,0,6],
           [0,8,0,0,4,0,0,0,0],
           [0,0,0,6,0,0,0,0,7],
           [1,0,0,0,0,0,0,0,9],
           [0,0,4,0,3,0,6,1,0]]


print(sudoku(puzzle))
