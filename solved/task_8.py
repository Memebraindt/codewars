"""
https://www.codewars.com/kata/52685f7382004e774f0001f7
Human Readable Time
"""

def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s // 3600, s // 60 % 60, s % 60)


print(make_readable(359999))
print(make_readable(3600))
print(make_readable(7225))
