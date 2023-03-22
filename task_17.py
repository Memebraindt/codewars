"""
https://www.codewars.com/kata/5324945e2ece5e1f32000370
Sum Strings as Numbers
"""


def sum_strings(x, y):
    st2 = ""
    c = 0
    lenx = len(x)
    leny = len(y)
    if lenx == 0 and leny == 0:
        return "0"
    if lenx != 0:
        while x[0] == "0":
            if len(x) == 1:
                break
            x = x[1:]
            lenx -= 1
    if leny != 0:
        while y[0] == "0":
            if len(y) == 1:
                break
            y = y[1:]
            leny -= 1
    x = "0" * (max(lenx, leny) - lenx) + x
    y = "0" * (max(lenx, leny) - leny) + y
    # print("x=", x)
    # print("y=", y)
    lenx = max(lenx, leny)
    leny = max(lenx, leny)
    for i in range(lenx - 1, -1, -1):
        a = int(x[i])
        b = int(y[i])
        if(a == "0") and (b == "0") and (c == "0"):
            break
        st2 = str((a+b+c) % 10) + st2
        c = (a + b + c) // 10
    if c != 0:
        st2 = str(c) + st2
    return st2


print(sum_strings("2", "9"))
print(sum_strings("2", "3"))
print(sum_strings("2", "999999999999999999999999999999999999999999"))
print(sum_strings("9999", "9999"))
print(sum_strings("08670", "0"))
print(sum_strings("", ""))
print(sum_strings("0", "0"))
print(sum_strings("00", ""))

