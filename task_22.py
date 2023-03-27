"""
https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7
Battleship field validator
"""


def validate_battlefield(field):
    count = [0] * 5
    for i in range(10):
        field[i].insert(0, 0)
    field.insert(0, [0] * 11)
    for i in range(1, 11):
        for j in range(1, 11):
            if field[i][j] != 0:
                field[i][j] += field[i - 1][j] + field[i][j - 1]
            if field[i][j] > 4:
                return False
                # raise RuntimeError("battleship is too big")
            count[field[i][j]] += 1
            if field[i - 1][j - 1] > 0 and field[i][j] > 0:
                return False
                # raise RuntimeError("wrong battleships configuration")
            elif field[i - 1][j] > 0 and field[i][j - 1] > 0:
                return False
                # raise RuntimeError("wrong battleships configuration")
    # print(field)
    # print(count)
    if count[4] != 1 or count[3] != 3 or count[2] != 6 or count[1] != 10 or count[0] != 80:
        return False
    return True


battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

test = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(validate_battlefield(battleField))
print(validate_battlefield(test))
