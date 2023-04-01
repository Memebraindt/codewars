def sort_array(arr):
    lst = []
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            lst.append(arr[i])
    lst.sort()
    k = 0
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            arr[i] = lst[k]
            k += 1
    return arr


print(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])

