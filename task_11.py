from itertools import permutations as prm

def permutations(s):
    return list(set("".join(x) for x in prm(s)))

print(permutations("aabb"))