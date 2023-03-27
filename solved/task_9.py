"""
https://www.codewars.com/kata/5287e858c6b5a9678200083c
Does my number look big in this?
"""


def narcissistic(val):
    return val == sum(int(x) ** len(str(val)) for x in str(val))


print(narcissistic(8))
print(narcissistic(371))
print(narcissistic(122))
print(narcissistic(4887))
