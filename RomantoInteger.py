class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev = res = 0
        for i in xrange(len(s)-1,-1,-1):
            value = dic[s[i]]
            if value < prev:
                res -= value
            else:
                res += value
            prev = value

        return res
        

"DCXXI"

        
        
        
        
        
        
        
        