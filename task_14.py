lst = [0, 1, 1, ]


def fib(n):
    last = len(lst)
    if last > n:
        return lst[n]
    else:
        for i in range(last, n+1):
            lst.append(lst[i-1] + lst[i-2])
        last = n
        return lst[n]


print(fib(5))
# print("lst = ", lst)
print(fib(100))
# print("lst = ", lst)
print(fib(1000))
# print("lst = ", lst)