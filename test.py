"""
https://www.codewars.com/kata/59568be9cc15b57637000054/train/python
BECOME IMMORTAL
"""


def elder_age(m, n, l, t):
    if max(n, m) - 1 < l:
        return 0
    ans = [[0, 0, 0], [0, 0, 1], [0, 1, 2]]
    if m < 3 and n < 3:
        return ans[m][n] if l == 0 else 0
    z, res = 2, 2
    while z < n and z < m:
        res = res * 4 + z ** 3 * 2
        z *= 2
        # print(f"res={res}, z={z}")
    min_nm = min(n, m)
    max_nm = max(n, m)
    if min_nm <= z < max_nm:
        div, mod = divmod(max_nm, z)
        print(f"div={div},mod={mod},z={z},res={res},-f(z)={(z * (z - 1) // 2) * (z - min_nm)},+f(z)="
              f"{(div * (div - 1) // 2 * (z ** 2) * min_nm) + (mod * min_nm * z)},min_nm={min_nm},max={max_nm}")
        return ((res - (z * (z - 1) // 2) * (z - min_nm)) * div + (div * (div - 1) // 2 * (z ** 2) * min_nm) +
                (mod * min_nm * z * div) + elder_age(mod, min_nm, l, t) +
                min_nm - z * min_nm * (min_nm - 1) // 2) % t
    else:
        dif_n, dif_m = z - n, z - m
        print(f"dif_n={dif_n}, dif_m={dif_m} f(z)=", (z * (z - 1) // 2) * (dif_n + dif_m))
        return res - (z * (z - 1) // 2) * (dif_n + dif_m) + elder_age(dif_m, dif_n, l, t)


# def elder_age(m, n, l, t):
#     ss = 0
#     for i in range(n):
#         for j in range(m):
#             a = max((i ^ j), 0)
#             ss = (ss + a) % t
#             # print(str(a).rjust(3, " "), end="")
#         # print()
#     # mx = max(n, m)
#     # mn = min(n, m)
#     # s = sum(range(1, mx)) - l*(mx-1)
#     # ss = s * mn
#     return ss

#
# print(elder_age(0, 0, 0, 10007))
# print(elder_age(1, 1, 0, 10007))
# print(elder_age(2, 2, 0, 10007))
# print(elder_age(4, 4, 0, 10007))
print(elder_age(3, 6, 4, 10007), " == 1?")
print(elder_age(5, 5, 3, 10007), " == 44?")
print(elder_age(8, 8, 0, 10007))
# print(elder_age(64, 64, 0, 1000007))
# print(elder_age(5, 2, 0, 1000007))
print(elder_age(5, 45, 3, 1000007), " == 4323")
print(elder_age(31, 39, 7, 2345), 1586)
print(elder_age(545, 435, 342, 1000007), 808451)
# print(elder_age(28827050410, 35165045587, 7109602, 13719506), 5456283)


# print(elder_age(8, 5, 1, 100))
# print(elder_age(5, 5, 0, 10007))
# print(elder_age(4, 16, 0, 10007))
# print(elder_age(128, 4, 0, 10007))
# print(elder_age(31, 39, 7, 2345))
# # print(elder_age(545, 435, 342, 1000007))
# print(elder_age(28827050410, 35165045587, 7109602, 13719506), " = ", 5456283)
