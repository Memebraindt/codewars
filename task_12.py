from itertools import combinations as cm

a = [["1", "2", "3"], ["4", "5", "6"],
     ["7", "8", "9"], ["99", "0", "99"]]
b = []


def add_lst(x, y, k):
    if (x < 0) or (x > 3) or (y < 0) or (y > 2):
        return -1
    if a[x][y] == "99":
        return -1
    b[k].append(a[x][y])


# def add_queue(lst, left, right):
#     if left > right:
#         return -1
#     for i in range(left, right):
#         add_queue(lst)


def get_pins(lst):
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
    d = ["".join(x) for x in [*b]]
    print("b = ", b)
    print("d = ", d)
    return d


print(get_pins("11"))
