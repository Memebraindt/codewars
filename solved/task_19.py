"""
https://www.codewars.com/kata/5877e7d568909e5ff90017e6
How many numbers III?
"""


def valid(summ, col, digit):
    if col < 0 or summ < 0:
        return False
    elif col != 0 and (summ/col > 9 or summ/col < digit):
        return False
    else:
        return True


def rec(number, digit, _sum, digits_left, answer, nmin, nmax):
    number = number * 10 + digit
    if _sum == 0 and digits_left == 0:
        if nmin == 0:
            nmin = number
        nmax = number
        print(f"line={number}, cur_digit={digit}, sum={_sum}, dig_left={digits_left}, ans={answer}, nmin={nmin}, nmax={nmax}")
        return [answer, nmin, nmax]

    if digits_left == 1 and digit <= _sum <= 9:
        answer += 1
        qq = rec(number, _sum, 0, 0, answer, nmin, nmax)
        answer = qq[0]
        nmin = qq[1]
        nmax = qq[2]
    if digits_left > 1:
        for i in range(digit, 10):
            if valid(_sum - i, digits_left - 1, i):
                qq = rec(number, i, _sum - i, digits_left - 1, answer, nmin, nmax)
                answer = qq[0]
                nmin = qq[1]
                nmax = qq[2]
    number = number // 10
    return [answer, nmin, nmax]


def find_all(sum_dig, digs):
    ans = [0]*3
    for i in range(1, 10):
        lst = rec(0, i, sum_dig - i, digs - 1, 0, 0, 0)
        ans[0] += lst[0]
        if ans[1] == 0:
            ans[1] = lst[1]
        if lst[2] != 0:
            ans[2] = lst[2]
    return ans if ans[0] != 0 else []


print(find_all(10, 3))
print(find_all(27, 3))
print(find_all(84, 4))
print(find_all(35, 6))
