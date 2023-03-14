# def narcissistic(val):
#     sval = str(val)
#     res = 0
#     for c in sval:
#         res += int(c) ** len(sval)
#     return False if res != val else True

def narcissistic(val):
    return val == sum(int(x) ** len(str(val)) for x in str(val))

print(narcissistic(8))
print(narcissistic(371))
print(narcissistic(122))
print(narcissistic(4887))