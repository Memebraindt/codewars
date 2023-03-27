"""
https://www.codewars.com/kata/52f677797c461daaf7000740
Smallest possible sum
"""

def solution(a):
    mx = 0
    mn = a[0]
    for i in range(len(a)):
        if a[i] > mx:
            mx = a[i]
        if a[i] < mn:
            mn = a[i]
    condition = False
    while not condition:
        flag = True
        for i in range(len(a)):
            if a[i] % mn == 0:
                a[i] = mn
            else:
                a[i] %= mn
                if a[i] < mn:
                    mn = a[i]
                flag = False
        condition = flag
    return mn*len(a)


print(solution([9]))
print(solution([6, 9, 21]))  # 9
print(solution([1, 21, 55]))  # 3
