

def addDigits(num):
    sum_ = 0
    if num > 9: 
        while num >= 1:
            sum_ += num % 10
            num //= 10
        return addDigits(sum_)
    else:
        return num

print addDigits(126)

# 1-29
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = 0
        while num > 0:            
            n += num%10
            num /= 10
            if num == 0:
                if n < 10:
                    return n
                else:
                    num = n
                    n = 0
print Solution().addDigits(38)