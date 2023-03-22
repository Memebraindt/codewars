"""
Next bigger number with the same digits
https://www.codewars.com/kata/55983863da40caa2c900004e
"""


def next_bigger(n):
    n = str(n)
    if len(n) == 1:
        return -1
    for i in range(len(n)-1, 0, -1):
        a = int(n[i])
        b = int(n[i - 1])
        _max = max(a, b)
        if a != _max:
            digits = [int(d) for d in (str(_max) + n[i+1:])]
            # print(digits)
            digits.sort()
            st2 = ''.join(str(d) for d in digits)
            st = n[:i-1] + n[i] + st2
            return int(st)
    return -1


print(next_bigger(154321))
print(next_bigger(59884848459853))
print(next_bigger(9876543210))
print(next_bigger(12))
print(next_bigger(2017))
print(next_bigger(1111))
print(next_bigger(0))

