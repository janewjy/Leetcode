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
# 2-6
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in xrange(2,n+1):
            for j in xrange(i):
                dp[i] += dp[j]*dp[i-j-1]
            
        return dp[n]
            
            