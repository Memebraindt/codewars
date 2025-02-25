def check(n, nx, ny, matrix) -> int:
    if not (0 <= nx < n and 0 <= ny < n):
        return -1   # выход за пределы диапазона
    else:
        return matrix[nx][ny]   # 1 - если клетка занята, 0 - если свободна

def get_new_direction(d):
    return (d + 1) % 4

def spiralize(n):
    matrix = [[0] * n for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y, d, pd = 0, 0, 0, 1
    dx, dy = directions[d]
    spiral_not_done = True 
    while spiral_not_done:
        matrix[x][y] = 1

        l1 = check(n, x + 2*dx, y + 2*dy, matrix) # смотрим через 1 клетку в том же направлении
        nd = get_new_direction(d)
        ndx, ndy = directions[nd]
        l2 = check(n, x + 2*ndx, y + 2*ndy, matrix) # смотрим через одну клетку в новом направлении

        """ Возможные значения l1 и l2 соответственно:
        [0, 0] - можно идти дальше
        [1, 0] - произойдёт самопересечение если продолжим двигаться дальше
        [-1 0] - выйдем за край через 2 хода
        [1 1] - дальше некуда идти. конец.
        check == -1 проверка на выход за край """
        if (l1 == 1 and l2 == 0) or check(n, x+dx, y+dy, matrix)==-1:
            if pd == 1:                             # если за два хода нужно сделать два поворота, то получается самопересечение, дальше не идём
                spiral_not_done = False    
            pd = 0
            d = get_new_direction(d)
            dx, dy = directions[d]
        elif l1 == l2 == 1 or matrix[x+dx][y+dy] == 1:               
            spiral_not_done = False
        x, y  = x + dx, y + dy
        pd += 1
    return matrix

# Проверка
size = 10
spiral = spiralize(size)
for row in spiral:
    print(row)
