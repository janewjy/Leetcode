class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = []
        each = []
        for i in xrange(1,numRows+1):
            if i == 1:
                res = [[1]]
                continue
            each = [0] * i
            for j in xrange(i):
                if j == 0 or j == i-1:
                    each[j] = 1
                else:
                    each[j] = res[-1][j-1] + res[-1][j]
            res.append(each)
        return res

        