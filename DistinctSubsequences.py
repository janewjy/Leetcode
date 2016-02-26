class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(t)
        n = len(s)
        dp = [[1]*(n+1) for _ in xrange(m+1)]
        for i in xrange(1,m+1):
            dp[i][0] = 0
        
        
        
        for i in xrange(m):
            for j in xrange(n):
                
                dp[i+1][j+1] = dp[i+1][j] + dp[i][j]*(s[j]==t[i])
                
        return dp[-1][-1]
            