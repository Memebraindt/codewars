"""
https://www.codewars.com/kata/52449b062fb80683ec000024
The Hashtag Generator
"""


def generate_hashtag(s):
    res = "#" + "".join(s.title().split())
    return res if 0 < len(res) <= 140 else False


print(generate_hashtag("Codewars Is Nice"))
print(generate_hashtag("CoDeWaRs is niCe"))
print(generate_hashtag('QmrYldaVnvV vmThwrEszZN UyxtrwIGlb  v uyK HUPNx vTUkunebYAg pTiCRFfjrPf Ohdj IEQOSX dxRrOkYslAS vZnEHzQwhoI fgTIHZjVbrm DgrBoHX jOG L dDbMubVjH'))

# def generate_hashtag(s):
#     ls = len(s)
#     if ls > 140 or ls == 0:
#         return False
#     else:
#         return "#" + "".join(s.title().split())

# def generate_hashtag(s):
#     res = "#" + "".join(s.title().split())
#     return False if len(s) == 0 or len(res) > 140 else res

