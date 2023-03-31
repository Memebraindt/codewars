"""
Next bigger number with the same digits
https://www.codewars.com/kata/55983863da40caa2c900004e
"""


def next_bigger(n):
    n = str(n)
    if len(n) == 1:
        return -1
    digits = [int(d) for d in n]
    for i in range(len(digits)-1, 0, -1):
        a = digits[i]
        b = digits[i - 1]
        if a > b:
            st = "".join(n[:i-1])
            lst = digits[i:]
            _min = lst[0]
            ind = 0
            for j in range(1, len(lst)):
                if (lst[j] > b) and (lst[j] < _min):
                    _min = lst[j]
                    ind = j
            num = str(_min)
            lst.pop(ind)
            lst.append(b)
            lst.sort()
            return int(st + num + "".join(str(j) for j in lst))
    return -1


print(next_bigger(15432))
print(next_bigger(59884848459853))
print(next_bigger(9876543210))
print(next_bigger(12))
print(next_bigger(2017))
print(next_bigger(1111))
print(next_bigger(0))
