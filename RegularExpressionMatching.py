class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        dp = [[None]*(n+1) for _ in xrange(m+1)]
        dp[0][0] = True
        stack = ['']
        for j in xrange(n):
            if p[j] == '*':
                dp[0][j+1] = dp[0][j-1]

        for i in xrange(m):
            for j in xrange(n):
                if p[j] == '*':
                    if dp[i+1][j-1]:
                        dp[i+1][j+1] = True
                    elif dp[i][j+1] and (p[j-1] == '.' or s[i] == p[j-1]):
                        dp[i+1][j+1] = True
                else:
                    if dp[i][j] and (s[i] == p[j] or p[j] == '.'):
                        dp[i+1][j+1] = True
        for i in dp:
            print i
        return dp[m][n]


        
        
print Solution().isMatch('aab','c*a*b')