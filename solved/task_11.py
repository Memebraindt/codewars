"""
https://www.codewars.com/kata/5254ca2719453dcc0b00027d
So Many Permutations
"""

from itertools import permutations as prm


def permutations(s):
    return list(set("".join(x) for x in prm(s)))


print(permutations("aabb"))