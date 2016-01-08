class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])

        dp = [[float('inf')]*(col+1) for _ in xrange(row+1)]
        dp[0][1] = 0
        print dp
        for i in xrange(1,row+1):
            for j in xrange(1,col+1):
                print dp[i][j-1]
                dp[i][j] = min(dp[i][j-1],dp[i-1][j]) + grid[i-1][j-1]
                print dp
        return dp[-1][-1]
a = Solution()
print a.minPathSum([[1,2,3,4],[5,6,7,8]])


