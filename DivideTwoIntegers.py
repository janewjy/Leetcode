class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return -1
        ad = abs(dividend)
        ar = abs(divisor)
        
        if ad < ar:
            return 0 
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1
        else:
            sign = 1
        tmp = ad
        count = 0
        while tmp >= ar:
            tmp -= ar
            count += 1
            tmpc = 1
            tar = ar
            while tmp >= tar:
                tmp -= tar
                count += tmpc
                tmpc += tmpc
                tar += tar
        if sign == -1:
            count = -count
            
        return min(max(count,  -2147483648),  2147483647)
            

# online better solution

class Solution:
# @return an integer
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

# faster solution
class Solution:
# @param {integer} dividend
# @param {integer} divisor
# @return {integer}
    def divide(self, dividend, divisor):
        MAX_INT=2147483647
        if divisor==0:
            return MAX_INT
        sign= dividend>0 and divisor>0 or dividend<0 and divisor<0
        dividend,divisor=abs(dividend),abs(divisor)
        res=0
        q=1
        dvs=divisor
        while dvs<dividend:
            dvs=dvs<<1
            q=q<<1
        while dvs>=divisor:
            if dividend>=dvs:
                dividend-=dvs
                res+=q
            q=q>>1
            dvs=dvs>>1
        res=res if sign else -res
        return min(res,MAX_INT)
# 1-27
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend >= 0 and divisor > 0 or (dividend <= 0 and divisor<0):
            sign = 1
        else:
            sign = -1
            
        dividend =abs(dividend)
        divisor = abs(divisor)
        
        res = 0
        while dividend >= divisor:
            time = divisor
            n = 1
            while dividend >= time:
                dividend -= time
                res += n
                n += n
                time += time
                
        if sign < 0:
            res = -res
        return min(max(-2147483648,res),2147483647)

import sys
print sys.maxint
print sys.maxint**10000