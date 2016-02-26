class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """


        n = x
        y = 1
        while x > y:
            print x, y
            x = (x+y)/2
            y = n/x
            print x, y
        return x

print Solution().mySqrt(5)

# binary search solution
import sys
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
             return 0 
        left = 1
        right = sys.maxint
        
        while left <= right:
            mid  = (left+right)/2
            if mid*mid > x:
                right = mid-1
            elif mid*mid <= x and (mid+1)**2>x:
                return mid
            else:
                left = mid +1
            
                
