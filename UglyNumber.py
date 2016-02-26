class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num > 0:
        
        
            while num%2  == 0:
            	num = num/2
            while num%3 == 0:
            	num = num/3
            while num%5 ==0:
            	num = num/5
            
        if num == 1 :
        	return True
        else:
        	return False
# 1-31
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num >= 0:
            while True:
                n = num
                for i in [2,3,5]:
                    if num%i == 0:
                        num/=i
                    if num == 1:
                        return True
                if n == num:
                    return False
        return False