class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        subtree = {0:1, 1:1,2:2}
        for i in xrange(1,n+1):
            if i not in subtree:
                print i
                num = 0
                for j in range(i):
                    num += subtree[i-1-j] * subtree[j]
                subtree[i] = num

        return subtree[n]

a = Solution()
print a.numTrees(7)
