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

# 2-8
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.res = 0
        self.m = m
        self.n = n
        self.res = self.path(1,1)
        return self.res       
        
    def path(self,i,j):
        if i >self.m or j> self.n:
            return 0
        if i == self.m and j == self.n:
            return self.res + 1
        return self.path(i+1,j) + self.path(i,j+1)
