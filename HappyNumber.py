class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        D = {}

        while n >= 1:
        	d = 0
        	while n > 0:
        		d += (n % 10)**2
        		
        		n //= 10
        	n = d
        	print d
        
        	if n == 1:
        		return True
        
        	elif n in D.keys():
        		return False
        		
        	else: 
        		D[n] = 1
# 1-31
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        table = {n:1}
        res = 0
        while True:
            while n > 0:
                digit = n%10
                res += digit*digit
                n /= 10
            if res == 1:
                return True
            else:
                if res not in table:
                    table[res] = 1
                    n = res
                    res = 0
                else:
                    return False