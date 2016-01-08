class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
    
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        ResGrid = [[0 for x in range(n+1)] for x in range(m+1)]
        ResGrid[0][1] = 1
    
        for i in range(1, m+1):
            for j in range(1, n+1):
                if not obstacleGrid[i-1][j-1]:
                    ResGrid[i][j] = ResGrid[i][j-1]+ResGrid[i-1][j]
        print ResGrid, obstacleGrid
    
        return ResGrid[m][n]

a = Solution()
test = [[0,0],[1,1],[0,0]]
test1 = [[0,0,0],[0,1,0],[0,0,0]]
print a.uniquePathsWithObstacles(test1)
