"""
https://www.codewars.com/kata/5324945e2ece5e1f32000370
Sum Strings as Numbers
"""


def sum_strings(x, y):
    len_x, len_y = len(x), len(y)
    max_len = max(len_x, len_y)
    x = x.rjust(max_len, "0")
    y = y.rjust(max_len, "0")
    len_x, len_y = max_len, max_len
    c_bit = 0
    rev_res = ""
    for i in range(len_x-1, -1, -1):
        digit_value = c_bit + int(x[i]) + int(y[i])
        c_bit, digit_value = divmod(digit_value, 10)
        rev_res += str(digit_value)
    rev_res += str(c_bit)[::-1]
    result = rev_res[::-1].lstrip("0")
    return "0" if result == "" else result


# print(str("0"))


#
# print(sum_strings("2", "999999999999999999999999999999999999999999"))
# print(sum_strings("9999", "9999"))
# print(sum_strings("08670", "0"))
print(sum_strings("", ""))
print(sum_strings("0", "0"))
print(sum_strings("00", ""))
print(sum_strings("0001", "1231451"))
# print(sum_strings("2", "12412414"))

