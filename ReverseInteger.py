class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            flag = 1
            x = abs(x)
        else:
            flag = 0
            
        rev = 0
        while x > 0:
            rev = rev*10 + x%10
            x //=10
            
        if rev < 2147483648:
            if flag:
                return 0-rev
            return rev
        return 0
# 1-24
import sys
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            sign = -1
        else:
            sign = 1
        
        x = abs(x)
        if int(str(x)[::-1]) > sys.maxint:
            return 0
        return int(str(x)[::-1])*sign
            