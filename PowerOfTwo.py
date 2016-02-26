# 1-26
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if x < 0 and n%2 != 0:
            sign = -1
        else:
            sign = 1
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            flag = -1
        else:
            flag = 1
            
        n = abs(n)
        x = abs(x)
        res = 1
        while n > 0:
            time = 1
            mul = x
            while n >= time:
                n -= time
                res *= mul
                time += time
                mul *= mul
        if flag == -1:
            res = 1.0/res
        if sign == -1:
            res = -res
        return min(max(-2147483648,res),2147483647)


        
        