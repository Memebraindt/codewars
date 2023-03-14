def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s // 3600, s // 60 % 60, s % 60)

# def make_readable(seconds):
#     sec = seconds % 60
#     mins = seconds // 60 % 60
#     hh = seconds // 3600
#     if sec<10:
#         sec = "0" + str(sec)
#     if mins<10:
#         mins = "0" + str(mins)
#     if hh < 10:
#         hh = "0" + str(hh)
#     sec = str(sec)
#     mins = str(mins)
#     hh = str(hh)
#     return hh + ":" + mins + ":" + sec

print(make_readable(359999))
print(make_readable(3600))
print(make_readable(7225))
