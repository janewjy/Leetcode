class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        rs = str(float(numerator)/denominator)
        pos = rs.find('.')
        s = rs[pos+1:]
        print s
        for i in range(len(s)/2 -1, -1, -1):
            if s


a = Solution()
a.fractionToDecimal(1,7)