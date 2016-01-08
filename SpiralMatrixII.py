class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[1]*n for _ in xrange(n)]
        a,b,c,d = 0, n-1, n-1, 0
        p = 0
        q = n
        k = 1
        while k < n*n + 1:
            for i in xrange(p,q):
                res[a][i] = k
                k += 1            
            a += 1
            for i in xrange(p+1,q):
                res[i][b] = k
                k += 1
            b -= 1
            for i in xrange(q-2, p-1,-1):
                res[c][i] = k
                k += 1
            c -= 1
            for i in xrange(q-2, p, -1):
                res[i][d] = k
                k += 1
            d += 1
            p += 1
            q -= 1

        return res
            
            

a = Solution()
print a.generateMatrix(5)