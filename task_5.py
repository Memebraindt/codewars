"""
https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
Mumbling
"""


def accum(s):
    return "-".join((c * i).title() for i, c in enumerate(s, 1))


print(accum("abcd"))
print(accum("RqaEzty"))
print(accum("cwAt"))
