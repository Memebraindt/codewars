"""
https://www.codewars.com/kata/5263c6999e0f40dee200059d
The observed PIN
"""

a = [["1", "2", "3"], ["4", "5", "6"],
     ["7", "8", "9"], ["99", "0", "99"]]
b = []
que = []
left, right = 0, 0


def add_lst(x, y, k):
    if (x < 0) or (x > 3) or (y < 0) or (y > 2):
        return -1
    if a[x][y] == "99":
        return -1
    b[k].append(a[x][y])


def add(elem, x, y):
    if x > y:
        return -1
    for i in range(x, y):
        que.append(str(que[i]) + str(elem))


def get_pins(lst):
    lst = str(lst)
    for x in range(len(lst)):
        b.append([])
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == lst[x]:
                    add_lst(i - 1, j, x)
                    add_lst(i + 1, j, x)
                    add_lst(i, j - 1, x)
                    add_lst(i, j + 1, x)
                    add_lst(i, j, x)
    for i in range(len(b[0])):
        que.append(b[0][i])
    left = 0
    right = len(b[0])
    for x in range(1, len(b)):
        for y in range(len(b[x])):
            add(b[x][y], left, right)
        dif = right - left
        left = right
        right += len(b[x]) * dif
    new_list = que[left:right]
    que.clear()
    b.clear()
    # print(que, left, right)
    return new_list


print(sorted(get_pins("8")))
print(sorted(get_pins("11")))
print(sorted(get_pins("369")))
