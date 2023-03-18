"""
https://www.codewars.com/kata/53d40c1e2f13e331fc000c26
The Millionth Fibonacci Kata
"""
import decimal
def fib(n):
    decimal.getcontext().prec = 100000
    root_5 = decimal.Decimal(5).sqrt()
    phi = ((1 + root_5) / 2)
    a = ((phi ** n) - ((-phi) ** -n)) / root_5
    return round(a)

print(fib(5))
print(fib(1))
print(fib(-2))
print(fib(5))
print(fib(-6))
print(fib(1000))
print(fib(-1000))



# left_num = 0
# left = 0
# mid = 1
# mid_num = 1
# right = 2
# right_num = 1
#
# def count_fib(n, l, m, r, lz, mz, rz):
#     res = 0
#     cur
#     if n > r:
#         for x in range(r, n+1):
#
#     return res
#
# def fib(n):
#     return count_fib(n, left, mid, right, left_num, mid_num, right_num)
#
#
# print(fib(5))
# print(fib(100))
# print(fib(1000))
