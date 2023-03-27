"""
Exes and Ohs
https://www.codewars.com/kata/55908aad6620c066bc00002a

"""


def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


print(xo("xxoo"))
print(xo("xxoasd1zxo"))
print(xo("xxoox"))
print(xo("xOOx"))