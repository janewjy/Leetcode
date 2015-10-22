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