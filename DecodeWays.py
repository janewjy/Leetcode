class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0' :
            return 0
        dic = {-1:1}
        for i in range(len(s)):
            if i == 0:
                dic[i] = 1
            elif s[i] != '0':
                dic[i] = dic[i-1]
            else:
                dic[i] = 0
            if len(s[i-1:i+1]) == 2 and '10' <= s[i-1:i+1] <= '26':
                dic[i] += dic[i-2]

        return dic[len(s) - 1]


a = Solution()
print a.numDecodings("01")        


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        dp = {-1:1,0:1}
        for i in xrange(1,len(s)):
            if s[i] != '0':
                dp[i] = dp[i-1]
            else:
                dp[i] = 0
            if 9<int(s[i-1:i+1]) < 27:
                dp[i] += dp[i-2]
        return dp[len(s)-1]
            
                
            