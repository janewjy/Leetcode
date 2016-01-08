class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == n:
            res = [[_ for _ in range(1,n+1)]]
            return res
        if k == 1:
            res = [[_] for _ in range(1,n+1)]
            return res

        res = self.combine(n-1,k-1)
        for i in res:
            i.append(n)
        res.extend(self.combine(n-1,k))
        return res

        

a = Solution()
print a.combine(4,2)