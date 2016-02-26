class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        island = 0
        n = len(grid)
        def sink(i,j):
            if i < 0 or i >= n or j < 0 or j>=len(grid[0]) or grid[i][j] == '0':
                return 0
            grid[i][j] = '0'
            sink(i+1,j),sink(i-1,j),sink(i,j+1),sink(i,j-1)
            return 1
            
                
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] != '0':
                    island += sink(i,j)
        return island