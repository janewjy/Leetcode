class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # too slow
        dic = {}
        count, result, l = 0, 0, 0
        

        while l < len(s):
            if s[l] not in dic:
                
                dic[s[l]] = l
                count += 1
                l += 1
            else:
                count = l - dic[s[l]] - 1 
                dic = {}
                l -= count
                count = 0
            

            result = max(count, result)
        
        return result

# Faster solution
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        start = result = 0
        usedChar = {}
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                result = max(result, i-start+1)
                
            usedChar[s[i]] = i
        return result

# 1-19 ??? use dictionary to solve it again
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j = 0, 0
        stack = []
        res = 0
        for i in xrange(len(s)):
            while j<i and s[i] in stack :
                stack.remove(s[j])
                j += 1
            stack.append(s[i])
            res = max(res, len(stack))
            
                        
        return res