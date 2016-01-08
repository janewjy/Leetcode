0.00001
2147483647

34.00515
-3


class Solution(object):

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        o = x
        res = 1
        if n < 0:
            sign = -1
        else:
            sign = 1
        n = abs(n)
        while n > 0:
            x = o             
            i = 1
            res *= x 
            n = n-i  
            while n - 2*i > 0:
                x *= x
                res *= x
                i += i
                n = n-i

        if sign == -1:
            return 1/res
        else:
            return res
# online
class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow

class Solution:
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)
a = Solution()
print a.myPow(34.00515,-3)