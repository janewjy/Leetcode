class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res1 = res2 = res3 = res4 = []




        while num >= 1000:
            res2.append('M')
            num -= 1000
        
        if num >= 900:
            res2.append('CM')
            num -= 900
        if num >= 500:
            res2.append('D')
            num -= 500
        if num >= 400:
            res2.append('CD')
            num -= 400
        while num >= 100:
            res2.append('C')
            num -= 100

        if num >= 90:
            res2.append('XC')
            num -= 90
        if num >= 50:
            res2.append('L')
            num -= 50
        if num >= 40:
            res2.append('XL')
            num -= 40
        while num >= 10:
            res2.append('X')
            num -= 10

        if num >= 9:
            res2.append('IX')
            num -= 9
        if num >= 5:
            res2.append('V')
            num -= 5
        if num >= 4:
            res2.append('IV')
            num -= 4
        while num >= 1:
            res2.append('I')
            num -= 1

        return "".join(res2)

a = Solution()
print a.intToRoman(0)

def intToRoman1(self, num):
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    res, i = "", 0
    while num:
        res += (num//values[i]) * numerals[i]
        num %= values[i]
        i += 1
    return res

def intToRoman(self, num):
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    res = ""
    for i, v in enumerate(values):
        res += (num//v) * numerals[i]
        num %= v
    return res