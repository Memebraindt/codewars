"""
https://www.codewars.com/kata/514b92a657cdc65150000006
Multiples of 3 or 5
"""


def solution(number):
    return sum([i if (i % 3 == 0) or (i % 5 == 0) else 0 for i in range(number)])


print(solution(4))
print(solution(-1))
print(solution(0))
print(solution(15))
print(solution(20))
print(solution(200))
