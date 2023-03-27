"""
https://www.codewars.com/kata/51b66044bce5799a7f000003
Roman Numerals Helper
"""
class RomanNumerals:
    lst = ["I", "V", "X", "L", "C", "D", "M"]
    num = [1, 5, 10, 50, 100, 500, 1000]
    lst1 = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    lst10 = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    lst100 = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    @staticmethod
    def to_roman(n):
        str2 = ""
        if n >= 1000:
            str2 += "M" * (n // 1000)
            n -= 1000 * (n // 1000)
        if n >= 100:
            str2 += RomanNumerals.lst100[n // 100 - 1]
            n -= 100 * (n // 100)
        if n >= 10:
            str2 += RomanNumerals.lst10[n // 10 - 1]
            n -= 10 * (n // 10)
        if n >= 1:
            str2 += RomanNumerals.lst1[n // 1 - 1]
            n -= n // 1
        return str2

    @staticmethod
    def from_roman(str1):
        xx = []
        for i in range(len(str1)):
            ind = RomanNumerals.num[RomanNumerals.lst.index(str1[i])]
            xx.append(ind)
        res = xx[-1]
        for x in range(len(xx)-1):
            if xx[x] < xx[x+1]:
                res -= xx[x]
            else:
                res += xx[x]
        return res


obj = RomanNumerals()
print(obj.from_roman('XXI'))
print(obj.to_roman(999))
print(obj.to_roman(1666))
print(obj.from_roman("MDCLXVI"))
print(obj.from_roman("MCDXLIV"))
print(obj.from_roman("M"))
print(obj.from_roman("L"))
print(obj.from_roman("I"))
