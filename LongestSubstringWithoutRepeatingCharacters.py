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