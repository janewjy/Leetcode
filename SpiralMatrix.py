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


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        while matrix:
            try:
                res.extend(matrix[0])
                matrix.remove(matrix[0])
                for i in xrange(len(matrix)):
                    res.append(matrix[i][-1])
                    matrix[i].remove(matrix[i][-1])
                res.extend(matrix[-1][::-1])
                matrix.remove(matrix[-1])
                for i in xrange(len(matrix)-1,-1,-1):
                    res.append(matrix[i][0])
                    matrix[i].remove(matrix[i][0])
            except:
                return res
        return res


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        res = []
        u,d,l,r = 0,len(matrix)-1,0,len(matrix[0])-1

        while u<d and l < r:
            res.extend([matrix[u][i] for i in xrange(l,r)])
            res.extend([matrix[i][r] for i in xrange(u,d)])
            res.extend([matrix[d][i] for i in xrange(r,l,-1)])
            res.extend([matrix[i][l] for i in xrange(d,u,-1)])
            u,d,l,r = u+1,d-1,l+1,r-1

        if u == d:
            res.extend([matrix[u][i] for i in xrange(l,r+1)])
        else:
            res.extend([matrix[i][l] for i in xrange(u,d+1)])
        return res