class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = bin(n)
        return s.count('1')
    
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            if n%2 == 1:
                count += 1
            n /= 2
            
        
        return count
    