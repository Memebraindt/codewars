"""
https://www.codewars.com/kata/585894545a8a07255e0002f1
Screen Locking Patterns
"""

from itertools import product

PASSWORD = {'A': ['B', 'BC', 'D', 'E', 'F', 'DG', 'H', 'EI'],
     'B': ['A', 'C', 'D', 'E', 'F', 'G', 'EH', 'I'],
     'C': ['BA', 'B', 'D', 'E', 'F', 'EG', 'H', 'FI'],
     'D': ['A', 'B', 'C', 'E', 'EF', 'G', 'H', 'I'],
     'E': ['A', 'B', 'C', 'D', ' E', 'F', 'G', 'H', 'I'],
     'F': ['A', 'B', 'C', 'ED', 'E', 'G', 'H', 'I'],
     'G': ['DA', 'B', 'EC', 'D', 'E', 'F', 'H', 'I'],
     'H': ['A', 'EB', 'C', 'D', 'E', 'F', 'G', 'I'],
     'I': ['EA', 'B', 'FC', 'D', 'E', 'F', 'HG', 'H']
     }


def get_ans(passw):
    return ["".join(p) for p in product(*(PASSWORD[int(d)] for d in passw))]


def count_patterns_from(firstPoint, length):
    if length == 0 or length > 9:
        return 0
    return get_ans()


print(count_patterns_from('A', 10), 0)
print(count_patterns_from('A', 0), 0)
print(count_patterns_from('E', 14), 0)
print(count_patterns_from('B', 1), 1)
print(count_patterns_from('C', 2), 5)
print(count_patterns_from('E', 2), 8)
print(count_patterns_from('E', 4), 256)
