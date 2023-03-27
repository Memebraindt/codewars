"""
https://www.codewars.com/kata/53d40c1e2f13e331fc000c26
The Millionth Fibonacci Kata
"""

import numpy as np
from numpy.compat import long


def fib(n):
    if -1 < n < 2:
        return n

    negative = n < 0
    n = abs(n)

    matrix_a = np.matrix([[0, 1], [1, 1]], dtype=object)
    pow_matrix = pow(matrix_a, n-1)
    res = pow_matrix * np.matrix([[0], [1]])
    if negative and n % 2 == 0:
        return -long(res[1])
    else:
        return long(res[1])


print(fib(5))
print(fib(-5))
print(fib(-1))
# print(fib(10000))
# print(fib(2000000))
# print(fib(-1000))
