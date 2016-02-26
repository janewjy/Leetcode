class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[0]*n for _ in xrange(m)]
        
        for i in xrange(m-1,-1,-1):
            for j in xrange(n-1,-1,-1):
                if i == m-1 and j == n-1:
                    dp[i][j] = max(1-dungeon[i][j],1)
                elif i == m-1:
                    dp[i][j] = max(1,dp[i][j+1]-dungeon[i][j])
                elif j == n-1:
                    dp[i][j] = max(1,dp[i+1][j]-dungeon[i][j])
                else:
                    dp[i][j] = max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1)
        return dp[0][0]
            
        