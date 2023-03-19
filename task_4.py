"""
Persistent Bugger
https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
"""


def persistence(n):
    ans = 0
    while len(str(n)) > 1:
        res = 1
        for c in str(n):
            res *= int(c)
        n = res
        ans += 1
    return ans


print(persistence(39))
print(persistence(4))
print(persistence(25))
print(persistence(999))
