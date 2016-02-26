
# 1-29
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            n = digits[i] + carry
            digits[i] = n%10
            carry = n//10
        if carry != 0:
            return [carry]+digits
        else:
            return digits
            
            
             