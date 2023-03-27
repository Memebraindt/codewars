def template(n):
    return [[i if i == j else 0 for i in range(1, n+1)] for j in range(1, n+1)]


print(template(7))

