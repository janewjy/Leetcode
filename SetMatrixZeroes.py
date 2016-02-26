class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        m = len(matrix)
        n = len(matrix[0])

        dici = []
        dicj = []


        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0 and i not in dici and j not in dicj:
                    dici.append(i)
                    dicj.append(j)
        for i in dici:
            matrix[i] = [0]*n
        for j in dicj:
            for i in xrange(m):
                matrix[i][j] = 0
