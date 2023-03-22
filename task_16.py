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


def print_res(res):
    for i in range(len(res)):
        print()
        for j in range(len(res[i])):
            print("{:18}".format(str(res[i][j])), end=", ")


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
                        # qq = qq.sort()
                        res[i].append(qq)
                    else:
                        res[i].append(qq[0])
                        puzzle[i][j] = qq[0]

        # uni_sqr =[[[0]*3]*3]
        print(res)
        for row in range(9):
            unique_row = [0] * 10
            for col in range(9):
                if isinstance(res[row][col], list):
                    for x in range(len(res[row][col])):
                        unique_row[res[row][col][x]] += 1

            print("row = ", row, "numb = ", unique_row)
            for uni_num in range(len(unique_row)):
                if unique_row[uni_num] == 1:
                    for y in range(9):
                        for z in range(len(res[row][y])):
                            if res[row][y][z] == uni_num:
                                res[row][y] = uni_num
                                puzzle[row][y] = uni_num
                                break

        for col in range(9):
            unique_col = [0] * 10
            for row in range(9):
                if isinstance(res[row][col], list):
                    for x in range(len(res[row][col])):
                        unique_col[res[row][col][x]] += 1

            print("col = ", col, "numb = ", unique_col)
            for uni_num in range(9):
                if unique_col[uni_num] == 1:
                    for xx in range(9):
                        if isinstance(res[xx][col], list):
                            print_res(puzzle)
                            for z in range(len(res[xx][col])):
                                if res[xx][col][z] == uni_num:
                                    print("xx, col = ", xx, col)
                                    res[xx][col] = uni_num
                                    puzzle[xx][col] = uni_num
                                    break

        #
        # for row in range(0, 9, 3):
        #     for col in range(0, 9, 3):
        #         for x in range(3):
        #             for y in range(3):
        #                 for z in range(len(res[row+x][col+y])):
        #                     uni_sqr[row][col].append(res[row+x][col+y][z])



        if upd == puzzle:
            print("Не нашёл решение :(")
            print_res(res)
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
