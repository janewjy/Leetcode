class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1]*n for _ in xrange(m)]
        for i in  xrange(1,m):
            for j in xrange(1,n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[-1][-1]

# linear space
class Solution(object):
    def uniquePaths(self, m, n):
        res = [1] * n
        for i in range(m-1):
            for j in range(1, n):
                res[j] += res[j-1]
        return res[-1]


a = Solution()
print a.uniquePaths(4,4)