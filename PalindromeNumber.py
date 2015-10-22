class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if 0 <= x <= 9:
            return True
        if x > 10 and x % 10 != 0:
            rev = 0
            while x > 0:
                rev = rev*10 + x % 10
                x //= 10
                see = rev*10 + x % 10
                if x == rev:
                    return True
                elif see == x:
                    return True
        return False
           
        