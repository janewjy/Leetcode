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
            
            

    def generateMatrix(self, n):
        A, lo = [], n*n+1
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [range(lo, hi)] + zip(*A[::-1])
            print A
        return A
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        A = [[n*n]]
        while A[0][0] > 1:
            A = [range(A[0][0] - len(A), A[0][0])] + zip(*A[::-1])
        return A * (n>0)
    def generateMatrix(self, n):
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in xrange(n*n):
            A[i][j] = k + 1
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A

a = Solution()
print a.generateMatrix(3)