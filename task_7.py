def move_zeros(lst):
    lst1, lst2 = [], []
    for x in lst:
        if x != 0:
            lst1.append(x)
        else:
            lst2.append(x)
    return lst1 + lst2


print(move_zeros([1, 2, 3, 0, 5, 3, 0, 1]))
