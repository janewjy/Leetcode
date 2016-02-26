class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        dp = [0]+[amount+1]*amount
        for i in xrange(1,amount+1):
            for value in coins:           
                if i-value >= 0:    
                    dp[i] = min(dp[i-value]+1,dp[i])
                else:
                    break
        if dp[amount] == amount+1:
            return -1
                             
        return dp[amount]
[1, 2, 5]
11

print Solution().coinChange([370,417,408,156,143,434,168,83,177,280,117],9953)            
