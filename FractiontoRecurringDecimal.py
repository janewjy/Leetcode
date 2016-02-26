class Solution(object):

    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        res = ''
        if numerator/denominator < 0:
            res += '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        if numerator%denominator == 0:
            res += str(numerator/denominator)
            return res
        res += str(numerator/denominator)
        res += '.'
        numerator %= denominator
        i = len(res)
        table = {}
        print res
        while numerator != 0:
            if numerator not in table:
                table[numerator] = i
            else:
                i = table[numerator]
                res = res[:i] +'(' + res[i:] + ')'
                return res
            numerator *= 10
            res += str(numerator/denominator)
            numerator %= denominator
            i += 1
        return res
        
        
        
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        if numerator == 0:
            return '0'
        if numerator*denominator > 0:
            sign = ''
        else:
            sign = '-'

        numerator, denominator = abs(numerator),abs(denominator)
        inter = int(numerator4/denominator)
        numerator = numerator3%denominator
        mapping = {numerator:0}
        decimal = []
        pos = 1
        while numerator!=0:
            digit = numerator/denominator
            decimal.append(str(digit))
            numerator%=denominator
            mapping(numerator:pos)












        integer = numerator/denominator
        numerator %= denominator
        mapping = {}
        pos = 0
        res = []
        while numerator*10%denominator not in mapping:
            digit = numerator*10/denominator
            mapping[digit] = pos
            res.append(str(digit))
            numerator = numerator*10%denominator
        res.insert(mapping[numerator*10%denominator],'(')
        
        return str(integer)+'.'+''.join(res)+')'

print Solution().fractionToDecimal(1,5)