class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        while matrix != []:
            try:
                res.extend(matrix[0])
                matrix.remove(matrix[0])
                res.extend([i[-1] for i in matrix])
                for i in matrix:
                    i.remove(i[-1])
                matrix[-1].reverse()
                res.extend(matrix[-1])
                matrix.remove(matrix[-1])
                res.extend([i[0] for i in reversed(matrix)])
                for i in matrix:
                    i.remove(i[0])
            except:
                return res
        return res

a = Solution()
print a.spiralOrder([[3],[2]])
[1,2,3],[4,5,6],[7,8,9]