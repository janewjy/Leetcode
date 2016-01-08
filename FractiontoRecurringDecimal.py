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
        
        
        