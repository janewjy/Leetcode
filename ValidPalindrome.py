# 1-26
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s = s.lower()
        i,j = 0, len(s)-1
        while i <= j:
            if not s[i].isalnum():
                i += 1 
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i]==s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True