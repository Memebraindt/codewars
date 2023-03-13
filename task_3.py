def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


print(xo("xxoo"))
print(xo("xxoasd1zxo"))
print(xo("xxoox"))
print(xo("xOOx"))